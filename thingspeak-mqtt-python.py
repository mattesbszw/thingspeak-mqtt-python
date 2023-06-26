import paho.mqtt.client as mqtt 
import json


MQTT_SERVER = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
MQTT_CHANNEL_ID = -1

MQTT_CLIENT_ID = ""
MQTT_USER = ""
MQTT_PASSWORD = ""

class ThingSpeakPayload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j) # deserializes binary json string from subscription into a dictionary
## end class definition

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("channels/" + str(MQTT_CHANNEL_ID) + "/subscribe")  # Subscribe to the topic 
## end on_connect function


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.

    print("Message received-> " + msg.topic)

    obj = ThingSpeakPayload(msg.payload)
    print(obj.channel_id)
    print(obj.created_at)
    print(obj.field1)
    print(obj.field2)
## end on_message function


## main routine

client = mqtt.Client(MQTT_CLIENT_ID) #create new instance
client.username_pw_set(username=MQTT_USER,password=MQTT_PASSWORD)

client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message

client.connect(MQTT_SERVER, MQTT_PORT)
client.loop_forever()  # Start networking daemon

