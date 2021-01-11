import time

from Backend.blockchain.Block import Block, GENESIS_DATA
from Backend.config import MINE_RATE, SECONDS
from Backend.util.hex_to_binary import hex_to_binary

def test_mine_block():
    """should be an instance of Block, match data and last block of genesis"""
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash
    assert hex_to_binary(block.hash)[0:block.difficulty] == '0' * block.difficulty

def test_genesis():
    """should be an instance of BLock, match every key value pair of GENESIS_DATA"""
    genesis = Block.genesis()

    assert isinstance(genesis, Block)

    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) == value

def test_quickly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'llll')
    mined_block = Block.mine_block(last_block, 'jd')

    assert mined_block.difficulty == last_block.difficulty + 1

def test_slowly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'llll')

    time.sleep(MINE_RATE / SECONDS)

    mined_block = Block.mine_block(last_block, 'jd')

    assert mined_block.difficulty == last_block.difficulty - 1

def test_mine_block_difficulty_limits_at_1():
    last_block = Block(
        time.time_ns(),
        'test_last_hash',
        'test_hash',
        'test_data',
        1,
        0
    )

    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine_block(last_block, 'jd')

    assert mined_block.difficulty == 1



