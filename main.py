from machine import Pin
from time import sleep as t

l = Pin(2, Pin.OUT)
interval = 2

while True:
    l.off()
    print('Led APAGADO')
    t(interval)
    l.on()
    print('Led ENCENDIDO')
    t(interval)
