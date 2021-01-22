import os
import random
import requests

from flask import Flask, jsonify, request
from flask_cors import CORS

from Backend.blockchain.Blockchain import Blockchain
from Backend.wallet.wallet import Wallet
from Backend.wallet.transaction import Transaction
from Backend.wallet.transaction_pool import TransactionPool
from Backend.pubsub import PubSub

app = Flask(__name__)
CORS(app, resourses={ r'/*' : { 'origins': 'https://zedchain.herokuapp.com/ ' } })
blockchain = Blockchain()
wallet = Wallet(blockchain)
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)

@app.route('/')
def default():
    return 'Welcome'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/range')
def route_blockchain_range():
    start = int(request.args.get('start'))
    end = int(request.args.get('end'))

    return jsonify(blockchain.to_json()[::-1 ][start:end])

@app.route('/blockchain/length')
def route_blockchain_length():
    return jsonify(len(blockchain.chain))

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = transaction_pool.transaction_data()
    transaction_data.append(Transaction.reward_transaction(wallet).to_json())
    blockchain.add_block(transaction_data)
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)
    transaction_pool.clear_blockchain_transactions(blockchain)

    return jsonify(block.to_json())

@app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
    transaction_data = request.get_json()
    transaction = transaction_pool.existing_transaction(wallet.address)

    if transaction:
        transaction.update(
            wallet, 
            transaction_data['recipient'],
            transaction_data['amount']
        )
    else:
        transaction = Transaction(
            wallet, 
            transaction_data['recipient'],
            transaction_data['amount']
        )

    pubsub.broadcast_transaction(transaction)

    print(f'transaction.to_json() : {transaction.to_json()}')
    return jsonify(transaction.to_json())

@app.route('/wallet/info')
def route_wallet_info():
    return jsonify({'address' : wallet.address, 'balance' : wallet.balance})

@app.route('/known-addresses')
def route_known_addresses():
    know_addresses = set()

    for block in blockchain.chain:
        for transaction in block.data:
            know_addresses.update(transaction['output'].keys())

    return jsonify(list(know_addresses))

@app.route('/transactions')
def route_transaction():
    return jsonify(transaction_pool.transaction_data())

ROOT_PORT = 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = result.get('https://zedchain.herokuapp.com/ ')

    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -> Successfully syncronized the local chain')
    except Exception as e:
        print(f'\n -> Error in syncroning the local chain : {e}')

if os.environ.get('SEED_DATA') == 'True':
    for i in range(10):
        blockchain.add_block([
            Transaction(Wallet(), Wallet().address, random.randint(2, 50)).to_json(),
            Transaction(Wallet(), Wallet().address, random.randint(2, 50)).to_json()
        ])

    for i in range(3):
        transaction_pool.set_transaction(
            Transaction(Wallet(), Wallet().address, random.randint(2, 50))
        )


app.run(port=PORT)
