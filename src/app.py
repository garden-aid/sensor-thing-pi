# Monitor temperature and report
import json
import os
import time

import grovepi
import iot

DHT_SENSOR_PORT = 7
DHT_SENSOR_TYPE = 0

def start(client_id):
    shadow_client = iot.create_shadow_client(
        os.environ.get('AWS_IOT_ENDPOINT'),
        os.environ.get('AWS_IOT_CA_CERT_PATH'),
        os.environ.get('AWS_IOT_KEY_PATH'),
        os.environ.get('AWS_IOT_COMBINE_CERT_PATH'),
        os.environ.get('RESIN_DEVICE_UUID')
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
