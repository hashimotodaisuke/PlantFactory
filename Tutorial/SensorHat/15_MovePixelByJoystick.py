from sense_hat import SenseHat
 
sh = SenseHat()
sh.clear()

x_min = 0
y_min = 0
x_max = 7
y_max = 7

x = x_min
y = y_min
sh.set_pixel(x, y, 255, 255, 255)

while True:
    for event in sh.stick.get_events():
        if event.action == 'pressed':
           sh.set_pixel(x, y, 0, 0, 0)
           if event.direction == 'up':
               if y == y_min:
                   y = y_max
               else:
                   y = y - 1

           if event.direction == 'down':
               if y == y_max:
                   y = y_min
               else:
                   y = y + 1

           if event.direction == 'left':
               if x == x_min:
                   x = x_max
               else:
                   x = x - 1

           if event.direction == 'right':
               if x == x_max:
                   x = x_min
               else:
                   x = x + 1

           if event.direction == 'middle':
               x = 0
               y = 0
           
           sh.set_pixel(x, y, 255, 255, 255)
