from src.blockchain import Chain, Block, GENESIS_BLOCK


def test_block_mine():
    last_block = GENESIS_BLOCK
    data = "test-data"
    block = Block.mine(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.previous_hash == last_block.hash
    assert block.hash[0:block.difficulty] == '0' * block.difficulty


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
