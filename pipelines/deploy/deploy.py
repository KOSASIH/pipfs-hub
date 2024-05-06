import subprocess

class Deploy:
    def __init__(self, project_dir, target_env):
        self.project_dir = project_dir
        self.target_env = target_env

    def deploy(self):
        """Deploy the project to the target environment."""
        deploy_command = f'mvn deploy -Dtarget-env={self.target_env}'
        subprocess.run(deploy_command, cwd=self.project_dir, shell=True)
