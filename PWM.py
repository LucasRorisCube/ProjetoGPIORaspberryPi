# Importa a biblioteca de GPIO para manipulação de leitura e escrita nos pinos da placa
import RPi.GPIO as GPIO
import time

# Funcao main
def main():

	# Pino onde o led esta
	led_pin = 20	

	# Inicializa a biblioteca de GPIO e desativa os Warnings de versão antiga
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_pin, GPIO.OUT)
	GPIO.setwarnings(False)

	# Cria um objeto de PWM com um máximo de 100 para o pino da led
	pwm = GPIO.PWM(led_pin, 100)

	# Inicia o PWM em 0% e varia dentre 0%, 25%, 50%, 75% e 100%
	pwm.start(0)
	for dc in [0, 25, 50, 75, 100]:
		pwm.ChangeDutyCycle(dc) # Seta o valor do PWM do pino da led
		time.sleep(1) # Aguarda 1 segundo para ter um tempo apropriado de visualizacao

# Executa indefinidamente a funcao main até que tenha uma interrupcao de teclado
try:
	while True:
		main()
# Limpa as configuracoes que fizemos nos pinos pela biblioteca GPIO quando o programa eh finalizado
except KeyboardInterrupt:
	GPIO.cleanup()


