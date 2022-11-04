from machine import Pin
from time import sleep_ms


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

def write_bytes(cte_byte: hex):
    pin3.value((cte_byte & 0b10000000) >> 7)
    pin4.value((cte_byte & 0b01000000) >> 6)
    pin5.value((cte_byte & 0b00100000) >> 5)
    pin6.value((cte_byte & 0b00010000) >> 4)
    pin7.value((cte_byte & 0b00001000) >> 3)
    pin8.value((cte_byte & 0b00000100) >> 2)
    pin9.value((cte_byte & 0b00000010) >> 1)
    pin10.value((cte_byte & 0b00000001) >> 0)


def off(delay: int):
    write_bytes(0x00)
    sleep_ms(delay)


def on_off_leds(delay: int):
    write_bytes(0xFF)
    sleep_ms(delay)
    write_bytes(0x00)
    sleep_ms(delay)


def nibbles(delay: int):
    write_bytes(0x0F)
    sleep_ms(delay)
    write_bytes(0xF0)
    sleep_ms(delay)


def half_nibbles_right(delay: int):
    write_bytes(0x03)
    sleep_ms(delay)
    write_bytes(0x0C)
    sleep_ms(delay)
    write_bytes(0x30)
    sleep_ms(delay)
    write_bytes(0xC0)
    sleep_ms(delay)
    

def half_nibbles_left(delay: int):
    write_bytes(0xC0)
    sleep_ms(delay)
    write_bytes(0x30)
    sleep_ms(delay)
    write_bytes(0x0C)
    sleep_ms(delay)
    write_bytes(0x03)
    sleep_ms(delay)


def shift_right(delay: int):
    write_bytes(0x80)
    sleep_ms(delay)
    write_bytes(0x40)
    sleep_ms(delay)
    write_bytes(0x20)
    sleep_ms(delay)
    write_bytes(0x10)
    sleep_ms(delay)
    write_bytes(0x08)
    sleep_ms(delay)
    write_bytes(0x04)
    sleep_ms(delay)
    write_bytes(0x02)
    sleep_ms(delay)
    write_bytes(0x01)
    sleep_ms(delay)

        
def shift_left(delay: int):
    write_bytes(0x01)
    sleep_ms(delay)
    write_bytes(0x02)
    sleep_ms(delay)
    write_bytes(0x04)
    sleep_ms(delay)
    write_bytes(0x08)
    sleep_ms(delay)
    write_bytes(0x10)
    sleep_ms(delay)
    write_bytes(0x20)
    sleep_ms(delay)
    write_bytes(0x40)
    sleep_ms(delay)
    write_bytes(0x80)
    sleep_ms(delay)


def zig_zag():
    shift_right(delay=200)
    shift_left(delay=200)


while True:
    ctrl = (pin2.value()*4) + (pin1.value()*2) + pin0.value()

    if ctrl == 0:
        off(500)
    if ctrl == 1:
        on_off_leds(500)
    if ctrl == 2:
        nibbles(200)
    if ctrl == 3:
        half_nibbles_right(200)
    if ctrl == 4:
        half_nibbles_left(200)
    if ctrl == 5:
        shift_right(200)
    if ctrl == 6:
        shift_left(200)
    if ctrl == 7:
        zig_zag()
