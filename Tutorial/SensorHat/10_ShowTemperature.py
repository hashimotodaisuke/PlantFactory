from sense_hat import SenseHat

sh = SenseHat()
while True:
    temp = sh.humidity
    messge = "{0:.1f}".format(temp)
    sh.show_message(messge)

