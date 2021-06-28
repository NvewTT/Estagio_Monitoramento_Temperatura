import random
from datetime import datetime
from paho.mqtt import client as mqtt_client


broker = '192.168.1.2'
port = 1883
topic = "home/sensor1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 10000)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time} {msg.payload.decode()} ºC ")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
