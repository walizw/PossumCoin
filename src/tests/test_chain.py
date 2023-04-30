from src.blockchain import Chain, Block, GENESIS_BLOCK
from src.config import MINE_RATE, SECONDS
from src.crypto import hex_to_binary

import time


def test_block_mine():
    last_block = GENESIS_BLOCK
    data = "test-data"
    block = Block.mine(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.previous_hash == last_block.hash
    assert hex_to_binary(block.hash)[
        0:block.difficulty] == '0' * block.difficulty


def test_chain_instance():
    chain = Chain()
    assert isinstance(chain, Chain)
    assert isinstance(chain.chain, list)
    assert isinstance(chain.chain[0], Block)
    assert chain.chain[0].hash == GENESIS_BLOCK.hash


def test_chain_add_block():
    chain = Chain()
    data = "test-data"
    chain.add_block(data)

    assert chain.chain[-1].data == data
    assert chain.chain[-1].previous_hash == chain.chain[-2].hash


def test_quickly_mined_block():
    last_block = Block.mine(GENESIS_BLOCK, "foo")
    mined_block = Block.mine(last_block, "bar")

    assert mined_block.difficulty == last_block.difficulty + 1


def test_slowly_mined_block():
    last_block = Block.mine(GENESIS_BLOCK, "foo")
    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine(last_block, "bar")

    assert mined_block.difficulty == last_block.difficulty - 1


def test_mined_block_difficulty_limits_at_1():
    last_block = Block(
        time.time_ns(),
        "test_last_hash",
        "test_data",
        "test_hash",
        1,
        0
    )

    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine(last_block, "bar")

    assert mined_block.difficulty == 1
