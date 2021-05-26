from time import sleep
from sense_hat import SenseHat

sh = SenseHat()
while True:
    humi = sh.temperature
    temp = sh.humidity
    pres = sh.pressure
    print('humidity {0:.1f}%, temperature {1:.1f}, pressure{2:.1f}'.format(humi, temp, pres))
    sleep(1) # wait 1 sec
