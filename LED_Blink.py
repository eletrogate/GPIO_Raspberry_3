#importa os módulos que serão utilizados
import gpiozero
import time

#instancia o led
led = gpiozero.LED(19)

while True:         #loop infinito
    led.on()            #acende o led
    time.sleep(1)    #aguarda 1 segundo
    led.off()            #apaga o led
    time.sleep(1)    #aguarda 1 segundo