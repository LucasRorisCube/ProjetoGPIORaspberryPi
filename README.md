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

# Pratica 3

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

No repositório há um arquivo chamado "hist.txt" que contém todos os comandos executados no terminal do linux durante essa prática.



