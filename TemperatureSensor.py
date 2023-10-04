from gpiozero import MotionSensor, LED
from signal import pause
from time import sleep

import RPi.GPIO as GPIO

import Adafruit_DHT

def main():
	
	GPIO.setwarnings(False)

	sensor = Adafruit_DHT.DHT11
	umidade, temp = Adafruit_DHT.read_retry(sensor, 14)
	print(f'temperatura: {float(temp)}ºC, umidade: {umidade}%')
	#print('Temp={0:0.1f}*C Umidade={1:0.1f}%'.format(temp, umidade))
	sleep(1)
	

try:
	while True:
		main()

except KeyboardInterrupt:
	GPIO.cleanup()


