from .block import Block


class Chain:
    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self) -> str:
        return f"Chain: {self.chain}"
