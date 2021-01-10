from Backend.blockchain.Blockchain import Blockchain
from Backend.blockchain.Block import GENESIS_DATA

def test_blockchain_insstance():
    """should match the hash value of genesis"""
    blockchain = Blockchain()

    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    """should add a new block"""
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data