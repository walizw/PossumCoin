from ..crypto import crypto_hash

import time


class Block:
    def __init__(self, timestamp: str, previous_hash: str, data: any, hash: str, difficulty: int, nonce: int):
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce

    @staticmethod
    def mine(last_block, data):
        timestamp = time.time_ns()
        previous_hash = last_block.hash
        difficulty = last_block.difficulty
        nonce = 0
        hash = crypto_hash(timestamp, previous_hash, data, difficulty, nonce)

        while hash[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            hash = crypto_hash(timestamp, previous_hash,
                               data, difficulty, nonce)

        return Block(timestamp, previous_hash, data, hash, difficulty, nonce)

    def __repr__(self) -> str:
        return (
            f"Block(\n"
            f"  timestamp={self.timestamp},\n"
            f"  previous_hash={self.previous_hash},\n"
            f"  data={self.data},\n"
            f"  hash={self.hash},\n"
            f"  difficulty={self.difficulty},\n"
            f"  nonce={self.nonce},\n"
            f")"
        )


GENESIS_BLOCK = Block(
    timestamp="1999-01-01T00:00:00.000000+00:00",
    previous_hash="",
    data="possums are so cute, and amazing and incredible and i love them so much and i want to hug them and kiss them.",
    hash="POSSUMSLOVER",
    difficulty=1,
    nonce="possum_nonce"
)
