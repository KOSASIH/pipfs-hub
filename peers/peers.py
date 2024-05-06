import ipfsapi

class Peers:
    def __init__(self, host='localhost', port=8080):
        self.ipfs = ipfsapi.connect(host=host, port=port)

    def list_peers(self):
"""List all the peers in the peer-to-peer network."""
        return self.ipfs.swarm.peers()

    def add_peer(self, peer_id):
        """Add a new peer to the peer-to-peer network."""
        return self.ipfs.swarm.add_peer(peer_id)

    def remove_peer(self, peer_id):
        """Remove a peer from the peer-to-peer network."""
        return self.ipfs.swarm.remove_peer(peer_id)
