# Projeto GPIO RaspberryPi
Projetos da disciplina de SEL0630 - Projetos em Sistemas Embarcados: Prática 1, 2 e 3

# Nome dos integrantes:

Gabriel Vinicius dos Santos (11819424)

Lucas Alves Roris (11913771)

# Prática 1

Primeiramente para esta prática, foi preciso instalar e configurar a Raspberry Pi 3 B+ presente no laboratório. Conectando a placa e executando o programa Raspberry Pi Imager, possível de ser baixada em https://www.raspberrypi.com/software/, o programa reconhece a placa e é possível instalar o Sistema Operacional Raspberry Pi OS.

Para acessar remotamente a placa, usamos o VNC (Virtual Network Computing) em que é possível fazer a transferência de arquivos e até observar a Interface gráfica da Raspberry Pi, desde que tanto a Raspberry Pi quanto o dispositivo que deseja consertar estejam na mesma rede Wi-Fi. Fizemos o acesso remoto também usando um celular na mesma rede wi-fi.

Sobre saídas retornadas e detalhes do hardware/arquitetura/kernel/GPIO, executamos os comandos no terminal do linux:

neofetch: ->  resumo das principais informações do hardware e SO presente na imagem abaixo.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/print_neofetch.png?raw=true)

ifconfig ->  exibe endereço de IP e MAC da Raspberry Pi presente na imagem abaixo.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/print_ifconfig.png?raw=true)

htop -> visualiza processos e recursos em sistemas unix presente na imagem abaixo.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/print_htop.png?raw=true)

pinout -> mostra as informações e numerações sobre a pinagem da Raspberry Pi presente na imagem abaixo.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/print_pinout.png?raw=true)

# Pratica 2

Sobre programação em Python para sistemas embarcados usando a GPIO da Raspberry, foram usadas duas bibliotecas, sendo delas RPi.GPIO e GPIO Zero. A segunda biblioteca é mais de alto nível e pode ser instalada com “pip install gpiozero”. Nela apenas podemos observar apenas as pinagens com GPIO, como observadas em https://pinout.xyz. Comandos como led=LED(17) para criar um objeto em python e led.on() e led.off() para piscar o Led numerado por 17 na numeração GPIO. Já a biblioteca RPi.GPIO pode ser instalada com “pip3 install RPi.GPIO” e nela podemos acessar os pinos de vários jeitos, como:
```python
GPIO.setmode(GPIO.BCM) # Define os pinos GPIO, semelhantemente a biblioteca anterior (https://pinout.xyz)
GPIO.setmode(GPIO.BOARD) # Deine os pinos de acordo com a pinagem da placa, sem usar a pinagem GPIO (https://pinout.xyz)

# Um simples Led piscante com essa biblioteca pode ser feito com:
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)
GPIO.output(18, False)
```

Além disso, vale ressaltar que foi usados os comandos `sudo apt install python3` para instalar o python no linux. Para o ambiente virtual, tivemos que instalar primeiramente com  `sudo pip install virtualenv` e depois `python3 -m venv 2471` para criar um ambiente virtual com nome 2471 e o comando `source 2471/bin/activate` para ativá-lo. Com isso foi possível instalar novas bibliotecas apenas no ambiente virtual criado, dentro da pasta “2471”. Com o comando `deactivate` podemos sair do ambiente virtual.

Sendo assim, foram mostrados exemplos de saídas digitais. Para leituras de I/O digital podemos usar ` GPIO.input(pin)` para checar se algum potão foi pressionado na primeira biblioteca e para a segunda biblioteca usamos `button = gpiozero.Button(2)` e `button.is_pressed` para checar se alguma entrada foi detectada. Um exemplo de detecção de eventos usando a primeira biblioteca é dado com `GPIO.add_event_detect(4, GPIO.BOTH,callback =button, bouncetime=200)`, em que o botão relacionado ao pino 4 recebe esse evento, e a função “button” em python executa se algo acontecer nesse pino. Com isso os eventos são semelhantes a interrupções previamente estudadas em outras disciplinas. Uma melhor explição visual das pinas é feita na imagem abaixo:

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/pinagem.png?raw=true)

Type-casting é usado para mudarmos a saida numérica para como gostariamos. Um Exemplo abaixo mostra o usado de Type casting:

```python
return "{:4d}{:02d}{:02d}".format(int(year),int(month),int(day))
```

Por fim,  exceção KeyboardInterrupt e GPIO cleanup se encontraram no exemplo abaixo:

```python
try:
	while True:
		main()
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
```

O código acima previne erros e espera o comando “Ctrl+C” para interromper a execução do programa. Quando a execução é interrompida a função `GPIO.cleanup()` limpa o pino, nao deixando em algum estado não requerido e evitando erros e warnings caso os pinos sejam usados para outros programas. Tudo comentado e explicado anteriormente foi usado na prática 2, principalmente o que está presente no código “contagem_regressiva.py”.

# Pratica 3

Para a Prática 3, tivemos contato com programação em Python de periféricos da Raspberry Pi para aplicações embarcados. Primeiramente fizemos um  PWM com RPi.GPIO, presente no código “PWM.py”. As principais funções são :

```python
led_pin = 20	
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm = GPIO.PWM(led_pin, 100)
pwm.start(0)
	for dc in [0, 25, 50, 75, 100]:
		pwm.ChangeDutyCycle(dc) 
		time.sleep(1) 
```

Sendo assim podemos variar o quanto queremos que a onda fique em HIGH ou LOW, de acordo com a porcentagem presente entre 0 e 100. 

Fizemos também um código usando um sensor infravermelho  presente em “InfraMotion.py”. As principais funções são:

```python
sensor_of_motion = MotionSensor(4) 
led = LED(20) 
sensor_of_motion.when_motion = led.on
sensor_of_motion.when_no_motion = led.off
pause()
```

Sendo assim, quando o sensor infravermelho capta movimento, ele liga o led presente no pino 20.

Por fim, um código um código para leitura de temperatura e umidade com DHT11 presente em “TemperatureSensor.py” em que as principais funções são:

```python
GPIO.setwarnings(False) 
sensor = Adafruit_DHT.DHT11 
umidade, temp = Adafruit_DHT.read_retry(sensor, 14) 
print(f'temperatura: {float(temp)}ºC, umidade: {umidade}%') 
sleep(1) 
```

Foi usado a biblioteca `import Adafruit_DHT`. Sendo assim, a cada 1 segundo, o sensor capta a umidade e temperatura com a função `Adafruit_DHT.read_retry` e imprime com a formatação correta devido ao uso de type-casting.

Abaixo, temos as imagens e resultados da terceira prática:

## Aplicação 1: PWM

O circuito abaixo foi construído e o código "PWM.py" foi executado, resultando nos 5 valores de tensão na saída do LED vistos pelo Osciloscópio.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/CircuitoLED_PWM.jpeg?raw=true)

Segue abaixo os 5 valores de PWM (0, 25%, 50%, 75%, 100%) vistos pelo osciloscópio.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/Osciloscopio_PWM_0.jpeg?raw=true)

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/Osciloscopio_PWM_25.jpeg?raw=true)

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/Osciloscopio_PWM_50.jpeg?raw=true)

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/Osciloscopio_PWM_75.jpeg?raw=true)

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/Osciloscopio_PWM_100.jpeg?raw=true)

## Aplicação 2: Sensor Proximidade

O circuito abaixo foi construído e o código "InfraMotion.py" foi executado. O resultado não pode ser mostrado por imagens, mas foi apresentado presencialmente para o professor.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/CircuitoSensorProximidade.jpeg?raw=true)

## Aplicação 3: Sensor de temperatura e Umidade DHT11

O circuito abaixo foi construído e o código "TemperatureSensor.py" foi executado, resultando na saída do terminal mostrada abaixo.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/CircuitoSHT11.jpeg?raw=true)

Segue abaixo o resultado após alguns segundos do programa executando.

![alt text](https://github.com/LucasRorisCube/ProjetoGPIORaspberryPi/blob/main/Images/ResultadoSensorTemperaturaHumidade.jpeg?raw=true)

## Observações

No repositório há arquivos chamados "hist_pratica1.txt", "hist_pratica2.txt" e "hist_pratica3.txt", que contém todos os comandos executados no terminal do linux durante cada prática.



