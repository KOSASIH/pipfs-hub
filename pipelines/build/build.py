import subprocess

class Build:
    def __init__(self, project_dir):
        self.project_dir = project_dir

    def build(self):
        """Build the project."""
        build_command = 'mvn clean package'
        subprocess.run(build_command, cwd=self.project_dir, shell=True)
