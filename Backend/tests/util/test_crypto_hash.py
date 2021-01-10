from Backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    """should return a hashed value"""
    assert crypto_hash(1, [2], 'three') == crypto_hash('three', 1, [2])