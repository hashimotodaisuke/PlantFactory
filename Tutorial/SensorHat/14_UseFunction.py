from time import sleep
from sense_hat import SenseHat
import sence_hat_function as func

sh = SenseHat()
message ='123456789'
func.show_message_with_delay(message, 0.5)
func.show_message_reverse(message, 0.5)
