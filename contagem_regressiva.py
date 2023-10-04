import RPi.GPIO as GPIO
import time



def contagem(number):
	div, rest = divmod(int(num), 60)

	while ((div >= 0) and (rest >= 0)):
		
		
		print(f'\rContagem regressiva ({div :02d}:{rest :02d})', end='')
		time.sleep(1)
		rest -= 1
		if rest < 0:
			rest = 59
			div -= 1
	print("\nAcendeu!")
	GPIO.output(5, GPIO.HIGH) #ou usar True


#########################################

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

# Led no port 5
GPIO.output(5, GPIO.LOW)

# Obtencao do valor
value = 0
while True:
	try:
		num = input("Digite o tempo da contagem em segundos: ")
		value = int(num)

		if value >= 0:
			break
		else:
			print('Positive Number please')
	except ValueError:
		print("Valid Number please")

# Realiza a contagem
contagem(value)

# Espera com o led ligado
try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
