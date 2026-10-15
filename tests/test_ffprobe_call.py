import os
import stat
import sys
import tempfile
import unittest

from tests import _stubs  # noqa: F401
import metadata

FAKE = """#!/bin/sh
# prints a minimal ffprobe xml, width = number of arguments received
cat <<XML
<ffprobe><streams><stream codec_type="video" width="$#" height="2"/></streams></ffprobe>
XML
"""


@unittest.skipIf(sys.platform == 'win32', 'uses a shell script as fake ffprobe')
class FfprobeArgsTest(unittest.TestCase):
    def test_all_arguments_reach_ffprobe(self):
        with tempfile.TemporaryDirectory() as d:
            exe = os.path.join(d, 'ffprobe')
            with open(exe, 'w') as f:
                f.write(FAKE)
            os.chmod(exe, os.stat(exe).st_mode | stat.S_IEXEC)
            m = metadata.MetaData.__new__(metadata.MetaData)
            m.meta = {'file': os.path.join(d, 'my file & (1).mov')}
            m.ffprobe_path = exe
            out = m.probe_ffprobe()
        self.assertEqual(out['error'], '')
        # ffprobe -show_streams -print_format xml -i <file> = 5 args
        self.assertEqual(out['width'], 5)

    def test_missing_ffprobe_reports_error(self):
        m = metadata.MetaData.__new__(metadata.MetaData)
        m.meta = {'file': 'x.mov'}
        m.ffprobe_path = ''
        out = m.probe_ffprobe()
        self.assertIn('not found', out['error'])


if __name__ == '__main__':
    unittest.main()
