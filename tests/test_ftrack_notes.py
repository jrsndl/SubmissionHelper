import logging
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import ftrack
import sequencer


class _Result:
    def __init__(self, items):
        self.items = items

    def first(self):
        return self.items[0] if self.items else None

    def all(self):
        return list(self.items)


class FakeSession:
    """answers the queries sequencer makes, records them"""

    def __init__(self, tasks=None, labels=None, shots=None):
        self.queries = []
        self.tasks = tasks or {}      # (shot, task) -> task dict
        self.labels = labels or {}    # name -> label dict
        self.shots = shots or {}      # shot -> shot dict

    def query(self, q):
        self.queries.append(q)
        if q.startswith('NoteLabel'):
            name = q.split('"')[1]
            return _Result([self.labels[name]] if name in self.labels else [])
        if q.startswith('Task'):
            parts = q.split('"')
            task, shot = parts[1], parts[3]
            t = self.tasks.get((shot, task))
            return _Result([t] if t else [])
        if q.startswith('Shot'):
            shot = q.split('"')[1]
            s = self.shots.get(shot)
            return _Result([s] if s else [])
        return _Result([])


def make_seq(settings, items, session):
    s = sequencer.Sequencer.__new__(sequencer.Sequencer)
    s.log = logging.getLogger('SubmissionHelper')
    s.headless = True
    s.ui = None
    s.in_path = ''
    base = {'ftrack_use': True, 'ftrack_project': 'Proj', 'ftrack_shot': '{shot}',
            'ftrack_task': '{task}', 'ftrack_include_2': '', 'ftrack_do_notes': True,
            'ftrack_do_op': False, 'ftrack_label_use': False, 'ftrack_label': '',
            'ftrack_version_use': False, 'ftrack_version': '',
            'ftrack_note_pattern': '(.*)', 'ftrack_note_repl': ''}
    base.update(settings)
    s.settings = {k: {'value': v} for k, v in base.items()}
    s.paths = {'FTRACK_SERVER': 'https://x', 'FTRACK_API_KEY': 'k', 'FTRACK_API_USER': 'u'}
    s.merged_list = items
    s.ftrack = {}
    patches = [mock.patch.object(sequencer, 'open_session', return_value=session),
               mock.patch.object(sequencer, 'find_project_id', return_value='pid' if session else None)]
    return s, patches


def note(content, label_ids=()):
    return {'content': content, 'note_label_links': [{'label_id': i} for i in label_ids]}


def run(s, patches):
    for p in patches:
        p.start()
    try:
        s.ftrack_query()
        s.select_ftrack_note()
    finally:
        for p in patches:
            p.stop()


class FtrackNotesTest(unittest.TestCase):

    def item(self, shot='sh010', task='comp', ext='exr', **kw):
        d = {'shot': shot, 'task': task, 'extension': ext, 'full_path': f'/x/{shot}_{task}.1001.{ext}'}
        d.update(kw)
        return d

    def test_notes_found_and_values_quoted(self):
        sess = FakeSession(tasks={('sh 010', 'comp'): {'id': 't1', 'notes': [note('hello')]}})
        s, p = make_seq({}, [self.item(shot='sh 010')], sess)
        with self.assertLogs('SubmissionHelper', 'DEBUG') as cm:
            run(s, p)
        self.assertEqual(s.merged_list[0]['ftrack_notes'], ['hello'])
        self.assertEqual(s.merged_list[0]['ftrack_note'], 'hello')
        task_q = [q for q in sess.queries if q.startswith('Task')][0]
        self.assertIn('name is "comp"', task_q)
        self.assertIn('parent.name is "sh 010"', task_q)
        self.assertIn('project.full_name is "Proj"', task_q)
        text = '\n'.join(cm.output)
        self.assertIn('1 with notes', text)
        self.assertIn('1 note(s) on task', text)
        rows = s.ftrack_table_rows()
        self.assertEqual(rows[0]['Status'], 'ok, 1 notes')
        self.assertEqual(rows[0]['Note'], 'hello')

    def test_label_filter_uses_label_ids(self):
        sess = FakeSession(
            tasks={('sh010', 'comp'): {'id': 't1', 'notes': [note('a', ['L1']), note('b', ['L2'])]}},
            labels={'For Client': {'id': 'L1'}})
        s, p = make_seq({'ftrack_label_use': True, 'ftrack_label': 'For Client'}, [self.item()], sess)
        run(s, p)
        self.assertEqual(s.merged_list[0]['ftrack_notes'], ['a'])

    def test_missing_label_warns_no_crash(self):
        sess = FakeSession(tasks={('sh010', 'comp'): {'id': 't1', 'notes': [note('a', ['L1'])]}})
        s, p = make_seq({'ftrack_label_use': True, 'ftrack_label': 'Nope'}, [self.item()], sess)
        with self.assertLogs('SubmissionHelper', 'WARNING') as cm:
            run(s, p)
        self.assertEqual(s.merged_list[0]['ftrack_notes'], [])
        self.assertIn("note label 'Nope' not found", '\n'.join(cm.output))

    def test_statuses_for_skipped_files(self):
        sess = FakeSession()
        items = [self.item(ext='mov'), self.item(), {'extension': 'exr', 'full_path': '/x/a.exr'}]
        s, p = make_seq({'ftrack_include_2': '.exr'}, items, sess)
        with self.assertLogs('SubmissionHelper', 'DEBUG') as cm:
            run(s, p)
        st = [r['Status'] for r in s.ftrack_table_rows()]
        self.assertEqual(st, ['skipped (extension)', 'task not found', 'template not resolved'])
        text = '\n'.join(cm.output)
        self.assertIn("extension 'mov' is not in Extensions", text)
        self.assertIn('No notes found', text)

    def test_summary_logged_once_when_unchanged(self):
        sess = FakeSession(tasks={('sh010', 'comp'): {'id': 't1', 'notes': [note('x')]}})
        s, p = make_seq({}, [self.item()], sess)
        with self.assertLogs('SubmissionHelper', 'INFO') as cm:
            run(s, p)
            run(s, p)
        summaries = [o for o in cm.output if 'Ftrack: project' in o]
        self.assertEqual(len(summaries), 1)

    def test_one_query_per_task(self):
        sess = FakeSession(tasks={('sh010', 'comp'): {'id': 't1', 'notes': []}})
        s, p = make_seq({}, [self.item(), self.item(), self.item()], sess)
        run(s, p)
        self.assertEqual(len([q for q in sess.queries if q.startswith('Task')]), 1)

    def test_ftrack_off_status_shown(self):
        s, p = make_seq({'ftrack_use': False}, [self.item()], None)
        run(s, p)
        self.assertIn("Use Ftrack", s.ftrack['status'])

    def test_nothing_to_query_is_explained(self):
        s, p = make_seq({'ftrack_do_notes': False}, [self.item()], FakeSession())
        with self.assertLogs('SubmissionHelper', 'INFO') as cm:
            run(s, p)
        self.assertIn('Query Notes', '\n'.join(cm.output))

    def test_project_not_found_warns(self):
        sess = FakeSession()
        s, p = make_seq({}, [self.item()], sess)
        p[1] = mock.patch.object(sequencer, 'find_project_id', return_value=None)
        with self.assertLogs('SubmissionHelper', 'WARNING') as cm:
            run(s, p)
        self.assertIn("project 'Proj' not found", '\n'.join(cm.output))

    def test_version_mode(self):
        sess = FakeSession(tasks={('sh010', 'comp'): {'id': 't1', 'notes': []}})
        versions = [{'version': 3, 'notes': [note('v3 note')]}, {'version': 2, 'notes': [note('v2')]}]
        orig = sess.query

        def query(q):
            if q.startswith('select asset.name'):
                sess.queries.append(q)
                return _Result(versions)
            return orig(q)
        sess.query = query
        items = [self.item(ver='2'), self.item(ver='7')]
        s, p = make_seq({'ftrack_version_use': True, 'ftrack_version': '{ver}'}, items, sess)
        run(s, p)
        self.assertEqual(items[0]['ftrack_notes'], ['v2'])
        self.assertEqual(items[1]['_ftrack_status'], 'version not found')

    def test_op_attrs(self):
        sess = FakeSession(tasks={('sh010', 'comp'): {'id': 't1', 'notes': []}},
                           shots={'sh010': {'id': 's1'}})
        s, p = make_seq({'ftrack_do_notes': False, 'ftrack_do_op': True}, [self.item()], sess)
        vals = {'framestart': 1001, 'frameend': 1100, 'handleStart': 8, 'handleEnd': 8}
        with mock.patch.object(sequencer.Sequencer, 'ftrack_get_hierarchical_attribute',
                               lambda self, sess, ent, key: vals[key]):
            run(s, p)
        it = s.merged_list[0]
        self.assertEqual(it['ftrack_shot_exists'], '1')
        self.assertEqual(it['ftrack_task_exists'], '1')
        # handles 8: 993-1108 without slate, the _slate tokens add the slate frame
        self.assertEqual(it['ftrack_op_start'], '993')
        self.assertEqual(it['ftrack_op_range'], '993-1108')
        self.assertEqual(it['ftrack_op_length'], '116')
        self.assertEqual(it['ftrack_op_start_slate'], '992')
        self.assertEqual(it['ftrack_op_range_slate'], '992-1108')
        self.assertEqual(it['ftrack_op_length_slate'], '117')
        self.assertEqual(s.ftrack_table_rows()[0]['Status'], 'ok')


if __name__ == '__main__':
    unittest.main()
