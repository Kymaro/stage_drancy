from grovepi import *
from grove_rgb_lcd import *
import time
from math import *


dht_sensor_port = 7
dht_sensor_type = 0

temp_sensor = 0
lum_sensor = 1
potentiometer = 2

button = 3
led = 4

B=4250
R0 = 100000


pinMode(button,"INTPUT")
pinMode(led,"OUTPUT")
pinMode(temp_sensor,"INTPUT")
pinMode(potentiometer,"INPUT")
pinMode(lum_sensor,"INTPUT")

t_refresh = 3000
t_actuator = 2000
temp_dht = 0
hum = 0
tempe = 0 
button_value = 1
lum = 0

adc_ref = 5
grove_vcc = 5
full_angle = 300

setText("Bienvenue\ndans l'IoT Hub")
setRGB(128,255,0)
time.sleep(2)

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
    	temperature()
	DHT() #A faire en dernier car un delai de retour de valeur digital
    	print(temp_dht)
    	print(hum)
    	print(tempe)
	t_refresh = 0   

    potentiometer_value = analogRead(potentiometer)
    voltage = round((float)(potentiometer_value)*adc_ref / 1023,2)
    degrees = round((voltage*full_angle)/grove_vcc,2)

    if degrees <= 100 and degrees >= 0 :
        setText("Temperature : \n" +str((tempe + temp_dht)/2.0))
        setRGB(0,128,255) 	
    elif degrees <= 200 and degrees > 100 :
        setText("Humidite : \n"+str(hum))
        setRGB(255,0,128)
    else :
        setText("Luminosite \n"+"Bouton :"+str(button_value))
        setRGB(255,128,0)
        
    time.sleep(50.0/1000.0)
    t_refresh += 100

"""
https://docs.microsoft.com/fr-fr/azure/iot-hub/iot-hub-python-getstarted
"""
