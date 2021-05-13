from sense_hat import SenseHat
sh=SenseHat()
while True:
    for event in sh.stick.get_events():
        if event.action == 'pressed':
           if event.direction == 'up':
               sh.show_letter('U', text_colour=[255, 255, 255])
           if event.direction == 'down':
               sh.show_letter('D', text_colour=[255, 0, 0])
           if event.direction == 'left':
               sh.show_letter('L', text_colour=[0, 255, 0])
           if event.direction == 'right':
               sh.show_letter('R', text_colour=[0, 0, 255])
        elif event.action == 'released':
            sh.clear()



