from .block import Block, GENESIS_BLOCK

class Chain:
    def __init__(self):
        self.chain = [GENESIS_BLOCK]

    def add_block(self, data):
        last_block = self.chain[-1]
        self.chain.append(Block.mine (last_block, data))

    def __repr__(self) -> str:
        return f"Chain: {self.chain}"
