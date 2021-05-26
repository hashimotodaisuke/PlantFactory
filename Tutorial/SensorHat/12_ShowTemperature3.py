from time import sleep
from sense_hat import SenseHat
from sence_hat_function import show_message_with_delay

sh = SenseHat()
while True:
    temp = sh.humidity
    message = "{0:.1f}".format(temp)
    show_message_with_delay(message, 0.5)

