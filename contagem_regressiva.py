# Importa as funcoes para manipulacao do tempo e dos pinos da Raspberry
import RPi.GPIO as GPIO
import time

# Funcao para escrever a contagem na tela da maneira especificada
def contagem(number):
	min, sec = divmod(int(number), 60) # Acha a quantidade de minutos e segundos para contagem

	# Conta ate chegar em zero
	while ((min >= 0) and (sec >= 0)):

		# Printa a contagem sempre na mesma linha
		print(f'\rContagem regressiva ({min :02d}:{sec :02d})', end='') 
		time.sleep(1) # Aguarda 1 segundo
		sec -= 1 # Diminui a contagem dos segundos
		if sec < 0: # Caso os segundos acabem, reseta os segundos e diminui os minutos
			sec = 59
			min -= 1
#########################################

pino_led = 5 # LED esta no pino 5

# Inicializa a biblioteca de GPIO e desativa os Warnings de versão antiga
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pino_led, GPIO.OUT)

# Desliga o LED
GPIO.output(pino_led, GPIO.LOW)

# Obtencao do valor pelo usuario ate ser um valor valido
value = 0
while True:
	try:
		num = input("Digite o tempo da contagem em segundos: ")
		value = int(num)

		if value >= 0:	# Caso for valido, procede para contagem
			break
		else:
			print('Digite um numero positivo por favor')
	except ValueError:
		print("Formato de numero invalido, tente novamente")

# Realiza a contagem
contagem(value)
# Quando acaba a contagem,  acende o LED
print("\nAcendeu!")
GPIO.output(pino_led, GPIO.HIGH)

# Espera com o led ligado ate uma interrupcao de teclado
try:
	while True:
		pass
# Limpa os pinos quando o programa acaba
except KeyboardInterrupt:
	GPIO.cleanup()
