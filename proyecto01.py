from machine import Pin
from utime import sleep_ms


pin25 = Pin(25, Pin.OUT)

pin0 = Pin(0, Pin.IN)
pin1 = Pin(1, Pin.IN)
pin2 = Pin(2, Pin.IN)

pin3 = Pin(3, Pin.OUT)
pin4 = Pin(4, Pin.OUT)
pin5 = Pin(5, Pin.OUT)
pin6 = Pin(6, Pin.OUT)
pin7 = Pin(7, Pin.OUT)
pin8 = Pin(8, Pin.OUT)
pin9 = Pin(9, Pin.OUT)
pin10 = Pin(10, Pin.OUT)

ctrl = 0

while True:
    pin25.toggle()
    ctrl = (pin2.value()*4) + (pin1.value()*2) + pin0.value()

    if ctrl == 0:
        pin3.value(0)
        pin4.value(0)
        pin5.value(0)
        pin6.value(0)
        pin7.value(0)
        pin8.value(0)
        pin9.value(0)
        pin10.value(0)
        sleep_ms(500)
    
    if ctrl == 1:
        pin3.value(1)
        pin4.value(1)
        pin5.value(1)
        pin6.value(1)
        pin7.value(1)
        pin8.value(1)
        pin9.value(1)
        pin10.value(1)
        sleep_ms(500)

    if ctrl == 2:
        pin3.value(1)
        pin4.value(1)
        pin5.value(1)
        pin6.value(1)
        pin7.value(0)
        pin8.value(0)
        pin9.value(0)
        pin10.value(0)
        sleep_ms(500)

    if ctrl == 3:
        pin3.value(0)
        pin4.value(0)
        pin5.value(0)
        pin6.value(0)
        pin7.value(1)
        pin8.value(1)
        pin9.value(1)
        pin10.value(1)
        sleep_ms(500)

    if ctrl == 6:
        pin10.toggle()
        sleep_ms(200)
        pin9.toggle()
        sleep_ms(200)
        pin8.toggle()
        sleep_ms(200)
        pin7.toggle()
        sleep_ms(200)
        pin6.toggle()
        sleep_ms(200)
        pin5.toggle()
        sleep_ms(200)
        pin4.toggle()
        pin3.toggle()
        sleep_ms(200)

    if ctrl == 7:
        pin3.toggle()
        sleep_ms(200)
        pin4.toggle()
        sleep_ms(200)
        pin5.toggle()
        sleep_ms(200)
        pin6.toggle()
        sleep_ms(200)
        pin7.toggle()
        sleep_ms(200)
        pin8.toggle()
        sleep_ms(200)
        pin9.toggle()
        pin10.toggle()
        sleep_ms(200)
