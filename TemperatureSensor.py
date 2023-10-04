# Importa as funcoes para manipulacao do sensor de temperatura e dos pinos da Raspberry
import RPi.GPIO as GPIO
import Adafruit_DHT

# Funcao principal
def main():
	
	GPIO.setwarnings(False) # Ignora os Warnings de versao

	sensor = Adafruit_DHT.DHT11 # Cria um objeto que consegue ler o valor do DHT11
	umidade, temp = Adafruit_DHT.read_retry(sensor, 14) # Le o valor de umidade e temperatura do sensor
	print(f'temperatura: {float(temp)}ºC, umidade: {umidade}%') # Printa no formato especificado
	sleep(1) # Delay de 1 segundo para nao sobrecarregar o sensor
	
# Deixa a funcao principal executando ate que seja detectado uma interrupcao do teclado
try:
	while True:
		main()
# Limpa os pinos quando o programa acaba
except KeyboardInterrupt:
	GPIO.cleanup()


