from sense_hat import SenseHat
sh = SenseHat()
while True:
    acceleration = sh.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    x=round(x, 2)
    y=round(y, 2)
    z=round(z, 2)
    print("x=%s, y=%s, z=%s" % (x, y, z))
