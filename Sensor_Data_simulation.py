import time
import json
import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "smart_dustbin/data"

client = mqtt.Client()
client.connect(BROKER, PORT)

def simulate_data():
    while True:
        data = {
            "fill_level": 80,  # Simulated value
            "temperature": 45.5  # Simulated value
        }
        client.publish(TOPIC, json.dumps(data))
        time.sleep(5)

simulate_data()
