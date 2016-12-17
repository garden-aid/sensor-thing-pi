# Monitor temperature and report
import time
import grovepi
import iot
import json

def load_config():
    with open('config.json') as data_file:
        return json.load(data_file)

CONFIG = load_config()

SHADOW_CLIENT = iot.create_shadow_client(
    CONFIG.endpoint,
    CONFIG.ca_path,
    CONFIG.key_path,
    CONFIG.cert_path,
    CONFIG.client_id
)

SHADOW_BOT = SHADOW_CLIENT.connect_to_shadow(SHADOW_CLIENT, 'garden-aid')

DHT_SENSOR_PORT = 7
DHT_SENSOR_TYPE = 0

while True:
    try:
         # Get the temperature and Humidity from the DHT sensor
        [TEMP, HUM] = grovepi.dht(DHT_SENSOR_PORT, DHT_SENSOR_TYPE)
        print("temp=", TEMP, "thumidity=", HUM, "%")

        # Report data to AWS
        SHADOW_STATE = '{"state":{"desired":{"temperature":' + TEMP + ', "humidity":' + HUM + '}}}'
        SHADOW_BOT.shadowUpdate(SHADOW_STATE, 5)

        # Sleep for 60 seconds
        time.sleep(60)
    except (IOError, TypeError) as err:
        print "Error"
