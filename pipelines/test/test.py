import subprocess

class Test:
    def __init__(self, project_dir):
        self.project_dir = project_dir

    def test(self):
        """Test the project."""
        test_command = 'mvn test'
        subprocess.run(test_command, cwd=self.project_dir, shell=True)
