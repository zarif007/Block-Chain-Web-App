import time

from Backend.util.crypto_hash import crypto_hash
from Backend.util.hex_to_binary import hex_to_binary
from Backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash', 
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonnce'
}

class Block:
    """Unit of storage in BlockChain that stores transictions"""

    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce
    
    def __repr__(self):
        """Block represntation"""

        return (
            'Block('
            f'TimeStamp -> {self.timestamp}, '
            f'Last_Hash -> {self.last_hash}, '
            f'Hash -> {self.hash}, '
            f'data -> {self.data} ) '
            f'difficulty -> {self.difficulty}, '
            f'nonce -> {self.nonce}'
        )
    
    @staticmethod
    def mine_block(last_block, data):
        """Mine a block based on the last given block and data, until a block
        has is found that meets leading 0's proof of work requirement."""
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """Generate the genesis block"""

        return Block(**GENESIS_DATA)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """"Calculate the adjust diffulty according to the MINE_RATE 
        Increase the difficulty for quickly mined blocks.
        Decrease otherwise"""

        if(new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1

        return max(1, last_block.difficulty - 1)


def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'haha')
    print(block)

if __name__ == '__main__':
    main()