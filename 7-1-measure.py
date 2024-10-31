import RPi.GPIO as gp
import time
import matplotlib.pyplot as plt

gp.setmode(gp.BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
gp.setup(leds, gp.OUT)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT, initial = gp.HIGH)
troyka = 13
comp = 14
gp.setup(comp, gp.IN)
gp.setup(troyka, gp.OUT)

def adc():
    perem = 255
    for i in range(7, -1, -1):
        perem -= 2 ** i
        gp.output(dac, dec2bin(perem))
        time.sleep(0.01)
        zn_comp = gp.input(comp)
        if zn_comp == 0:
            perem += 2 ** i
    return perem

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    results = []
    t_start = time.time()
    c = 0
    v = 0
    gp.output(troyka, gp.HIGH)
    while v < 256*0.8:
        v = adc()
        print(v)
        results.append(v)
        time.sleep(0)
        c += 1
        gp.output(leds, dec2bin(v))
    gp.output(troyka, gp.LOW)
    while v > 256*0.2:
        v = adc()
        print(v)
        results.append(v)
        time.sleep(0)
        c += 1
        gp.output(leds, dec2bin(v))
    t_finish = time.time()
    fin_time = t_finish - t_start
    with open('data.txt', 'w') as f:
        f.write('\n'.join(str(results)))
    
    y = [i/256*3.3 for i in results]
    x = [i*fin_time/c for i in range(len(results))]
    plt.plot(x, y)
    plt.xlabel('время')
    plt.ylabel('напряжение')
    plt.show()
finally:
    gp.output(leds, 0)
    gp.output(dac, 0)
    gp.cleanup()