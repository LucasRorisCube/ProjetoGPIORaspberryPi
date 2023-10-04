import RPi.GPIO as GPIO
import time

def main():
	
	led_pin = 20	
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_pin, GPIO.OUT)
	GPIO.setwarnings(False)

	pwm = GPIO.PWM(led_pin, 100)
	pwm.start(0)
	

	for dc in [0, 25, 50, 75, 100]:
		pwm.ChangeDutyCycle(dc)
		time.sleep(1)

try:
	while True:
		main()

except KeyboardInterrupt:
	GPIO.cleanup()


