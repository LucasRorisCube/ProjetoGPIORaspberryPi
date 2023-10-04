from gpiozero import MotionSensor, LED
from signal import pause


def main():
	
	
	pir = MotionSensor(4)
	led = LED(20)

	pir.when_motion = led.on
	pir.when_no_motion = led.off

	pause()
	

try:
	while True:
		main()

except KeyboardInterrupt:
	GPIO.cleanup()


