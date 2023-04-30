class Block:
    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"Block - data: {self.data}"
