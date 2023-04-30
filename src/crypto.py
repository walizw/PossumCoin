import hashlib


def crypto_hash(data) -> str:
    return hashlib.sha256(str(data).encode('utf-8')).hexdigest()
