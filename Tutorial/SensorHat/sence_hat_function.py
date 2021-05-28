from sense_hat import SenseHat
from time import sleep

sh = SenseHat()
def show_message_with_delay(message, delay):
    for moji in message:
        sh.show_letter(moji)
        sleep(delay)

def show_message_reverse(message, delay):
    for moji in reversed(message):
        sh.show_letter(moji)
        sleep(delay)
