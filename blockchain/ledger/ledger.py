import hashlib
import time

class Ledger:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the genesis block of the blockchain."""
        genesis_block = {
            'index': 0,
            'timestamp': int(time.time()),
            'data': 'Genesis Block',
            'previous_hash': '0' * 64
        }
        self.chain.append(genesis_block)

    def calculate_hash(self, block):
        """Calculate the hash of a block."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_block(self, data):"""Add a new block to the blockchain."""
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': int(time.time()),
            'data': data,
            'previous_hash': self.calculate_hash(previous_block)
        }
        self.chain.append(new_block)
