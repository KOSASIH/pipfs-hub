import docker

class Docker:
    def __init__(self):
        self.client = docker.from_env()

    def list_containers(self):
        """List all the running containers."""
        return self.client.containers.list()

    def start_container(self, container_id):
        """Start a container."""
        self.client.containers.get(container_id).start()

    def stop_container(self, container_id):
        """Stop a container."""
        self.client.containers.get(container_id).stop()
