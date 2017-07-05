from grovepi import *
from grove_rgb_lcd import *
import time,datetime,json
from math import *
from util import *


dht_sensor_port = 7
dht_sensor_type = 0

temp_sensor = 0
lum_sensor = 1
potentiometer = 2

button = 3
led = 4

B=4250
R0 = 100000

ID = getId()

pinMode(button,"INTPUT")
pinMode(led,"OUTPUT")
pinMode(temp_sensor,"INTPUT")
pinMode(potentiometer,"INPUT")
pinMode(lum_sensor,"INTPUT")
time.sleep(1)

t_refresh = 3000
t_actuator = 2000
temp_dht = 0
hum = 0
tempe = 0 
mode_value = 0
lum = 0


adc_ref = 5
grove_vcc = 5
full_angle = 300

setText("Bienvenue\ndans l'IoT Hub")
setRGB(128,255,0)
time.sleep(2)

def DHT() : #temperature et humidite analogique
    global temp_dht,hum
    [temp_dht,hum] = dht(dht_sensor_port,dht_sensor_type)
    temp_dht = round(temp_dht,1)

def Temperature() : #capteur de temperature analogique
    global tempe
    analog_value = analogRead(temp_sensor)
    R = 1024.0/analog_value - 1.0
    tempe = 1.0/(log(R)/B + 1/298.15) - 273.15
    tempe= round(tempe,1)

def PotentiometerToDegrees(potentiometer_value) : #convertie la valeur du potentiometre en degree
    voltage = round((float)(potentiometer_value)*adc_ref / 1023,2)
    degrees = round((voltage*full_angle)/grove_vcc,2)
    return degrees

<<<<<<< HEAD
def screen_administrator() : # permet de gerer lécran sans quil refresh a chaque iteration 
=======
def screen_administrator() : # permet de gerer lecran sans quil refresh a chaque iteration 
>>>>>>> 93847698ef234a77b7c059993b9f0611afcad4a9
    global mode_value
    average_degrees = 0
    for i in range(10) :
        value = PotentiometerToDegrees(analogRead(potentiometer))
        average_degrees += value / 10.0
        time.sleep(1.0/1000.0)

        

    print(average_degrees)
<<<<<<< HEAD
    if average_degrees != 152.4 : # valeur qui apparait a chaque nouvel appel des valeurs des capteurs
=======
    if not(average_degrees <= 154.0 and average_degrees >= 151.0) : # valeur qui apparait a chaque nouvel appel des valeurs des capteurs
>>>>>>> 93847698ef234a77b7c059993b9f0611afcad4a9
    	if (average_degrees <=100 and average_degrees >= 0) and mode_value != 1 : #MODE 1
        	setText("Temperature : \n" +str((tempe + temp_dht)/2.0))
        	setRGB(0,128,255)
        	mode_value = 1
    	elif (average_degrees <= 200 and average_degrees > 100) and mode_value != 2 : #MODE 2
        	setText("Humidite : \n"+str(hum))
        	setRGB(255,0,128)
        	mode_value = 2
    	elif (average_degrees > 200 and average_degrees <=300) and mode_value != 3 : # MODE 3
        	setText("Luminosite \n")
        	setRGB(255,128,0)
        	mode_value = 3   

while True :

    if ( t_refresh >= t_actuator) : 
    	Temperature()
	DHT() #A faire en dernier car un delai de retour de valeur digital
    	print(temp_dht)
    	print(hum)
    	print(tempe)
	t_refresh = 0 
        dt = str(datetime.datetime.now())
        d = {'DeviceID' : ID, 'Temperature' : (tempe + temp_dht)/2.0) , 'Humidity' : hum,'Time' : dt }
        msg = json.dumps(d)
        print(msg)
    screen_administrator()
    time.sleep(50.0/1000.0)
    t_refresh += 100

"""
https://docs.microsoft.com/fr-fr/azure/iot-hub/iot-hub-python-getstarted
http://www.stevenfowler.me/p/send-raspberry-pi-data-azuure/
"""
