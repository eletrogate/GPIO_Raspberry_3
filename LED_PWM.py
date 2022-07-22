#importa os módulos que serão utilizados
import gpiozero
import time

#instancia o led
led = gpiozero.PWMLED(26)

while True:              #loop infinito
    for i in range(11):          #faz 10 ciclos
                                  #incrementando i
                                  #em 1 a cada ciclo
        led.value = i / 10      #define o duty-cicle
        time.sleep(0.1)          #aguarda 0.1 segundos
    for i in range(11):          #faz o mesmo ciclo
        led.value = (10 - i) / 10 #define o duty-cicle
        time.sleep(0.1)          #aguarda 0.1 segundos