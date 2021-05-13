from time import sleep
from sense_hat import SenseHat
import get_data

sensor = SenseHat()

def setText(text):
    sensor.show_message(text)
    
def get_output(output):
    setText(output)

def main():
    while True:
        humi, temp = get_data.read()
        text = 'humi {0:.1f}% temp {1:.1f}*'.format(humi, temp)
        setText(text)
        sleep(1)

if __name__ == '__main__':
    main()
