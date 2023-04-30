from .block import Block, GENESIS_BLOCK


class Chain:
    def __init__(self):
        self.chain = [GENESIS_BLOCK]

    def add_block(self, data):
        last_block = self.chain[-1]
        self.chain.append(Block.mine(last_block, data))

    def replace_chain(self, chain: list):
        if len(chain) <= len(self.chain):
            raise Exception(
                "Cannot replace. The incoming chain must be longer.")

        try:
            Chain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f"Cannot replace. The incoming chain is invalid.")

        self.chain = chain

    @staticmethod
    def is_valid_chain(chain) -> bool:
        if chain[0] != GENESIS_BLOCK:
            raise Exception("The genesis block must be valid.")

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid(last_block, block)

        return True

    def __repr__(self) -> str:
        return f"Chain: {self.chain}"
