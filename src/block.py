from .crypto import crypto_hash

import datetime


class Block:
    def __init__(self, timestamp: str, previous_hash: str, data: any, hash: str):
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.hash = hash

    @staticmethod
    def mine(last_block, data):
        return Block(
            timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            previous_hash=last_block.hash,
            data=data,
            hash=crypto_hash(data)
        )

    def __repr__(self) -> str:
        return (
            f"Block(\n"
            f"  timestamp={self.timestamp},\n"
            f"  previous_hash={self.previous_hash},\n"
            f"  data={self.data},\n"
            f"  hash={self.hash}\n"
            f")"
        )


GENESIS_BLOCK = Block(
    timestamp="1999-01-01T00:00:00.000000+00:00",
    previous_hash="",
    data="possums are so cute, and amazing and incredible and i love them so much and i want to hug them and kiss them.",
    hash="POSSUMSLOVER"
)
