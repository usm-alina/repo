import RPi.GPIO as gp
from time import sleep

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
gp.setup(troyka, gp.OUT, initial = gp.HIGH)
gp.setup(comp, gp.IN)

def adc():
    perem = 255
    for i in range(7, -1, -1):
        perem -= 2 ** i
        gp.output(dac, dec2bin(perem))
        sleep(0.1)
        zn_comp = gp.input(comp)
        if zn_comp == 0:
            perem += 2 ** i
    return perem

try:
    while True:
        v = adc()
        if v != 0:
            print('напряжение:', v * 3.3 / 256)
        gp.output(dac, 0)
        sleep(0.1)

finally:
    gp.output(dac, 0)
    gp.cleanup