import time

from Backend.util.crypto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash', 
    'hash': 'genesis_hash',
    'data': []
}

class Block:
    """Unit of storage in BlockChain that stores transictions"""
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.data = data
        self.hash = hash
    
    def __repr__(self):
        """Block represntation"""
        return (
            'Block('
            f'TimeStamp -> {self.timestamp}, '
            f'Last_Hash -> {self.last_hash}, '
            f'Hash -> {self.hash}, '
            f'data -> {self.data} )'
        )
    
    @staticmethod
    def mine_block(last_block, data):
        """Mine a block based on the last given block and data"""
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        """Generate the genesis block"""
        return Block(**GENESIS_DATA)


def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'haha')
    print(block)

if __name__ == '__main__':
    main()