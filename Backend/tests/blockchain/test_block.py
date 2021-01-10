from Backend.blockchain.Block import Block, GENESIS_DATA

def test_mine_block():
    """should be an instance of Block, match data and last block of genesis"""
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash

def test_genesis():
    """should be an instance of BLock, match every key value pair of GENESIS_DATA"""
    genesis = Block.genesis()

    assert isinstance(genesis, Block)

    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) == value



