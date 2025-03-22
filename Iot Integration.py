import paho.mqtt.client as mqtt
import json
import requests

# MQTT configuration
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "smart_dustbin/data"

# Flask server API
SERVER_URL = "http://127.0.0.1:5000/update"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        requests.post(SERVER_URL, json=data)
    except Exception as e:
        print(f"Error: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()
