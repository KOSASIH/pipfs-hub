from kubernetes import client, config

class Kubernetes:
    def __init__(self):
        config.load_kube_config()
        self.api_instance = client.CoreV1Api()

    def list_pods(self):
        """List all the running pods."""
        return self.api_instance.list_pod_for_all_namespaces(watch=False)

    def create_pod(self, pod_spec):
        """Create a new pod."""
        return self.api_instance.create_namespaced_pod(namespace="default", body=pod_spec)

    def delete_pod(self, pod_name):
        """Delete a pod."""
        self.api_instance.delete_namespaced_pod(name=pod_name, namespace="default", body=client.V1DeleteOptions())
