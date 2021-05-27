from time import sleep
from sense_hat import SenseHat # refer https://pythonhosted.org/sense-hat/api/#joystick

sh=SenseHat()
while True:
    event = sh.stick.get_events()
    if event:
        # print( event[0].action, event[0].direction)
        print( '%s-%s' %(event[0].action, event[0].direction))
    sleep(0.3)
