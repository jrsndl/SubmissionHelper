
import logging
import os
import platform
import subprocess

class Deadline(object):

    def __init__(self, gui, pths):
        self.log = logging.getLogger("mylog")
        self.settings = gui
        self.paths = pths
        self.ayon_csv = None

        if not self.are_paths_ok():
            return

    def are_paths_ok(self):

        to_check = ['ayon', 'deadline', 'AYON_SERVER_URL', 'AYON_USERNAME', 'AYON_API_KEY', 'FTRACK_SERVER', 'FTRACK_API_KEY', 'FTRACK_API_USER']
        errors = 0
        for k in to_check:
            value = self.paths.get(k)
            if k == k.lower():
                if value is None or value == "":
                    self.log.error(f"Can't find valid {k} path!")
                    errors += 1
            else:
                if value is None or value == "":
                    self.log.error(f"Can't find valid environment variable {k}")
        return True

    def external_execute(self, args):
        kwargs = {
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "text": True  # Automatically decodes to string
        }
        if platform.system().lower() == "windows":
            kwargs["creationflags"] = (
                    subprocess.CREATE_NEW_PROCESS_GROUP
                    | getattr(subprocess, "DETACHED_PROCESS", 0)
                    | getattr(subprocess, "CREATE_NO_WINDOW", 0)
            )
        popen = subprocess.Popen(args, **kwargs)
        popen_stdout, popen_stderr = popen.communicate()
        if popen_stdout:
            self.log.info(popen_stdout)
        if popen_stderr:
            self.log.error(f"Error: {popen_stderr}")

        # Check the return code
        if popen.returncode != 0:
            self.log.error(f"Command failed with return code {popen.returncode}")

    def build_ayon_csv(self, csv_path, project, folder='', task=''):
        self.csv_path = csv_path
        self.csv_name = os.path.basename(csv_path).strip(".csv")
        self.ayon_csv = [
            self.paths['ayon'],
            'addon',
            'traypublisher',
            'ingestcsv',
            '--filepath',
            csv_path,
            '--project',
            project,
            '--folder-path',
            folder,
            '--task',
            task,
            '--ignore-validators'
        ]

    def publish_local(self):

        if not self.are_paths_ok():
            return
        if self.ayon_csv is None:
            return

        my_env = os.environ
        # AYON FTRACK
        my_env["FTRACK_SERVER"] = self.paths['FTRACK_SERVER']
        my_env["FTRACK_API_KEY"] = self.paths['FTRACK_API_KEY']
        my_env["FTRACK_API_USER"] = self.paths['FTRACK_API_USER']
        # AYON SERVER
        my_env["AYON_USERNAME"] = self.paths['AYON_USERNAME']
        my_env["AYON_API_KEY"] = self.paths['AYON_API_KEY']

        popen = subprocess.Popen(self.ayon_csv, env=my_env)
        popen_stdout, popen_stderr = popen.communicate()
        ret_code = popen.returncode
        if popen_stdout:
            print("stdout:")
            print(popen_stdout.decode("utf-8"))
        if popen_stderr:
            print("stderr:")
            print(popen_stderr.decode("utf-8"))

        return ret_code

    def publish_deadline(self):

        envs = ["FTRACK_SERVER", "FTRACK_API_KEY", "FTRACK_API_USER", "AYON_USERNAME", "AYON_API_KEY"]
        envs_list = []
        for i, one in enumerate(envs):
            val = self.paths.get(one)
            if val is not None:
                envs_list.append("-prop")
                envs_list.append(f"EnvironmentKeyValue{str(i)}={one}={val}")

        params_1 = [
            self.paths['deadline'], '-SubmitCommandLineJob', '-executable', self.paths['ayon'].replace("/", "\\"),
            '-pool', self.settings['dead_primpool']['value'],
            '-group', self.settings['dead_group']['value'],
            '-priority', str(self.settings['dead_priority']['value']),
            '-department', self.settings['dead_department']['value'],
            '-prop', f"LimitGroups={self.settings['dead_limits']['value']}",
            "-prop", f"OutputDirectory0={self.csv_path}"
        ]
        params_1.extend(envs_list)

        # the deadline arguments have to be quoted, so pre-joining here
        # since there is executable already in params_1, removing path to ayon
        deadline_args = " ".join(self.ayon_csv[1:])
        params_2 = [
            '-name', self.csv_name,  # id
            '-arguments', deadline_args
        ]
        print(f"Submitting job: {params_1 + params_2}")
        self.external_execute(params_1 + params_2)

