from Backend.wallet.wallet import Wallet

def test_verify_valid_signature():
    data = {'kire' : 'kmn asos?'}
    wallet = Wallet()

    signature = wallet.sign(data)

    assert Wallet.verify(wallet.public_key, data, signature)

def test_verify_invalid_signature():
    data = {'kire' : 'kmn asos?'}
    wallet = Wallet()

    signature = wallet.sign(data)

    assert not Wallet.verify(Wallet().public_key, data, signature)
    