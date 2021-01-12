import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from Backend.blockchain.Block import Block


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-f41bde00-54c5-11eb-bfb3-7239c411611a'
pnconfig.publish_key = 'pub-c-9b242c62-0451-4a2c-a955-86d2aa6fc8ca'


CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}

class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self, pubnub, message_object):
        print(f'\n -> Channel: {message_object} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n-->successfully replaced a chain')
            except Exception as e:
                print(f'\n --> Did not replace chain: {e}')


class PubSub():
    """Handles the publish/subscribe layer of the application
    Provides communication between nodes of the blockchain network"""

    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

    def publish(self, channel, message):
        """Publish the message object to the channel"""
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """Broadcast a block object to all nodes"""
        self.publish(CHANNELS['BLOCK'], block.to_json())


def main():
    pubsub = PubSub()

    time.sleep(1) 

    pubsub.publish(CHANNELS['TEST'], {'yoyo' : 'JD'})


    

if __name__ == '__main__':
    main()