import ipfsapi

class DFS:
    def __init__(self, host='localhost', port=8080):
        self.ipfs = ipfsapi.connect(host=host, port=port)

    def add_file(self, file_path):
        """Add a file to the distributed file system."""
        return self.ipfs.add(file_path)

    def get_file(self, file_hash):
        """Get a file from the distributed file system."""
        return self.ipfs.cat(file_hash)

    def list_files(self):
        """List all the files in the distributed file system."""
        return self.ipfs.ls()
