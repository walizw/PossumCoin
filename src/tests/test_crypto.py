from src.crypto import crypto_hash, hex_to_binary


def test_crypto_hash():
    assert crypto_hash(
        "foo") == "b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b"
    assert crypto_hash("foo") == crypto_hash("foo")
    assert crypto_hash("foo") != crypto_hash("bar")
    assert crypto_hash(1, [2], "three") == crypto_hash("three", 1, [2])


def test_hex_to_binary():
    n = 123456789
    h = hex(n)[2:]
    b = hex_to_binary(h)

    assert int(b, 2) == n
