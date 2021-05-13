from time import sleep
from sense_hat import SenseHat
import set_display

sensor = SenseHat()

def read():
    humi = sensor.temperature
    temp = sensor.humidity    
    return humi, temp

def main():
    while True:
        humi = sensor.temperature
        temp = sensor.humidity
        # pres = sensor.pressure
        text = 'humi {0:.1f}% temp {1:.1f}*'.format(humi, temp)
        set_display.get_output(text)
        print('humidity {0:.1f}%, temperature {1:.1f}'.format(humi, temp))
        sleep(1)

if __name__ == '__main__':
    main()
