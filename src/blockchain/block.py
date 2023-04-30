from ..crypto import crypto_hash, hex_to_binary
from src.config import MINE_RATE

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
        difficulty = Block.adjust_diff(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, previous_hash, data, difficulty, nonce)

        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_diff(last_block, timestamp)
            hash = crypto_hash(timestamp, previous_hash,
                               data, difficulty, nonce)

        return Block(timestamp, previous_hash, data, hash, difficulty, nonce)

    @staticmethod
    def adjust_diff(last_block: int, new_timestamp: int) -> int:
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1

        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

        return 1

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
    timestamp=time.time_ns(),
    previous_hash="",
    data="possums are so cute, and amazing and incredible and i love them so much and i want to hug them and kiss them.",
    hash="POSSUMSLOVER",
    difficulty=1,
    nonce="possum_nonce"
)
