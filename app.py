from grovepi import *
from grove_rgb_lcd import *

dht_sensor_port = 7
dht_sensor_type = 0

while True:
	try:
		[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)		#Get the temperature and Humidity from the DHT sensor
		print("temp =", temp, "C\thumidity =", hum,"%") 	
		# t = str(temp)
		# h = str(hum)
		
		# setRGB(0,128,64)
		# setRGB(0,255,0)
		# setText("Temp:" + t + "C      " + "Humidity :" + h + "%")			
	except (IOError,TypeError) as e:
		print("Error")