# Monitor temperature and report
import json
import os
import time

import grovepi
import iot

def load_config():
    file_name = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(file_name) as data_file:
        return json.load(data_file)


DHT_SENSOR_PORT = 7
DHT_SENSOR_TYPE = 0

def start(client_id):
    config = load_config()

    shadow_client = iot.create_shadow_client(
        config.endpoint,
        config.ca_path,
        config.key_path,
        config.cert_path,
        config.client_id
    )

    shadow = shadow_client.connect_to_shadow(shadow_client, client_id)

    while True:
        try:
            # Get the temperature and Humidity from the DHT sensor
            [temp, hum] = grovepi.dht(DHT_SENSOR_PORT, DHT_SENSOR_TYPE)
            print("temp=", temp, "thumidity=", hum, "%")

            # Report data to AWS
            shadow_state = '{"state":{"desired":{"temperature":' + temp + ', "humidity":' + hum + '}}}'
            shadow.shadowUpdate(shadow_state, 5)

            # Sleep for 60 seconds
            time.sleep(60)
        except (IOError, TypeError) as err:
            print 'Error during measurement:', err

try:
    start('garden-aid')
except (IOError) as err:
    print 'Error during startup:', err
