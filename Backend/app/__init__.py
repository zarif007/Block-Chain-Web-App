import os
import random
import requests

from flask import Flask, jsonify

from Backend.blockchain.Blockchain import Blockchain
from Backend.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)

@app.route('/')
def default():
    return 'Welcome'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    trasaction_data = 'stubbed_transaction_data'

    blockchain.add_block(trasaction_data)

    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())

ROOT_PORT = 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = result.get(f'http://localhost:{ROOT_PORT}/blockchain')

    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -> Successfully syncronized the local chain')
    except Exception as e:
        print(f'\n -> Error in syncroning the local chain : {e}')


app.run(port=PORT)
