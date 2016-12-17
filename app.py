import time
import grovepi

DHT_SENSOR_PORT = 7
DHT_SENSOR_TYPE = 0

while True:
    try:
         # Get the temperature and Humidity from the DHT sensor
        [TEMP, HUM] = grovepi.dht(DHT_SENSOR_PORT, DHT_SENSOR_TYPE)
        print("temp=", TEMP, "thumidity=", HUM, "%")
        time.sleep(60)
    except (IOError, TypeError) as err:
        print "Error"
