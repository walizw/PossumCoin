from .blockchain.chain import Chain

import paho.mqtt.client as mqtt

import readline
import threading
import time

readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode emacs")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}\nMessage: {msg.payload.decode()}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

threading.Thread(target=client.loop_forever).start()

time.sleep(0.1)

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
    elif line[0] == "subscribe":
        if len(line) < 2:
            print("Usage: subscribe [topic]")
            continue

        client.subscribe(line[1])
        time.sleep(0.1)
    elif line[0] == "publish":
        if len(line) < 3:
            print("Usage: publish [topic] [message]")
            continue

        client.publish(line[1], line[2])
        time.sleep(0.1)

client.disconnect()
