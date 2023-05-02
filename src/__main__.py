from .blockchain import Block, Chain

import paho.mqtt.client as mqtt

import threading
import time
import json

client = mqtt.Client()
blockchain = Chain()


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("possumcoin/block")


def on_message(client, userdata, msg):
    if msg.topic == "possumcoin/block":
        block = Block.from_json(json.loads(msg.payload))
        possible_chain = blockchain.chain[:]
        possible_chain.append(block)

        try:
            blockchain.replace_chain(possible_chain)
            print("The chain was replaced successfully.")
        except Exception as e:
            print(f"Could not replace chain: {e}")


client.on_connect = on_connect
client.on_message = on_message

CONNECTED = False


def mine_block(chain: Chain, transaction_data: str):
    chain.add_block(transaction_data)
    print(f"A block was mined successfully.")

    client.publish("possumcoin/block", chain.chain[-1].to_json())


while True:
    line = input(">>> ").split(" ")
    if len(line) == 0:
        continue

    if line[0] == "exit":
        break
    elif line[0] == "help":
        print("\t\t> PossumCoin <\n")
        print("Commands:")
        print("- help: show this screen")
        print("- subscribe [topic]: subscribe to a topic")
        print("- publish [topic] [message]: publish a message to a topic")
        print("- exit: exits the program")
    elif line[0] == "connect":
        if len(line) < 3:
            print("Usage: connect [host] [port]")
            continue
        elif CONNECTED:
            print("You are already connected to a broker!")
            continue

        client.connect(line[1], int(line[2]))
        threading.Thread(target=client.loop_forever).start()
        time.sleep(0.1)
        CONNECTED = True
    elif line[0] == "mine":
        if not CONNECTED:
            print("You are not connected to a broker!")
            continue

        threading.Thread(target=mine_block, args=(blockchain, "test")).start()
    elif line[0] == "chain":
        for block in blockchain.chain:
            print(block.hash)

client.disconnect()
