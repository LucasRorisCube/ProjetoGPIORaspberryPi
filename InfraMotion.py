# Importa as funcoes para manipulacao de leds e sensor de movimento
from gpiozero import MotionSensor, LED
from signal import pause

# Funcao principal
def main():
	
	sensor_of_motion = MotionSensor(4) # Define que o pino analogico do sensor de presenca esta no pino 4 da Raspberry
	led = LED(20) # Define que o pino do LED esta no pino 20 da Raspberry

	# Define que quando o sensor detecta movimento, o LED deve ligar
	sensor_of_motion.when_motion = led.on

	# Define que quando o sensor nao detecta movimento, o LED deve desligar
	sensor_of_motion.when_no_motion = led.off

	# Pausa o programa
	pause()

# Deixa a funcao principal executando ate que seja detectado uma interrupcao do teclado
try:
	while True:
		main()
# Limpa os pinos quando o programa acaba
except KeyboardInterrupt:
	GPIO.cleanup()


