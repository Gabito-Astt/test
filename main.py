from machine import Pin
from time import sleep as t

l = Pin(2, Pin.OUT)
interval = 1

while True:
    l.off()
    print('Led OFF')
    t(interval)
    l.on()
    print('Led ON')
    t(interval)