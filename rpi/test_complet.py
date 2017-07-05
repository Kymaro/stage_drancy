from grovepi import *
from grove_rgb_lcd import *
import time
from math import *


dht_sensor_port = 7
dht_sensor_type = 0

temp_sensor = 14
lum_sensor = 1

button = 3
led = 4

B=4250
R0 = 100000


pinMode(button,"INTPUT")
pinMode(led,"OUTPUT")
pinMode(temp_sensor,"INTPUT")

t_refresh = 3000
t_actuator = 3000
temp_dht = 0
hum = 0
tempe = 0 
button_value = 0
lum = 0

setText("Bienvenue\ndans l'IoT Hub")
setRGB(128,255,0)
time.sleep(5)

def DHT() :
    global temp_dht,hum
    [temp_dht,hum] = dht(dht_sensor_port,dht_sensor_type)

def temperature() :
    global tempe
    analog_value = analogRead(temp_sensor)
    R = 1024.0/analog_value - 1.0
    tempe = 1.0/(log(R)/B + 1/298.15) - 273.15

while True :

    if ( t_refresh >= t_actuator) : 
    	DHT()
    	#temperature()
    	print(temp_dht)
    	print(hum)
    	#print(temp)
	    print(analogRead(temp_sensor))
    	t_refresh = 0
    time.sleep(1)


"""
https://docs.microsoft.com/fr-fr/azure/iot-hub/iot-hub-python-getstarted
"""
