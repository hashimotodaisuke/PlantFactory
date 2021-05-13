from time import sleep
from sense_hat import SenseHat
sh = SenseHat()
 
r = [255,0,0]       #red
o = [255,127,0]     #orainge
y = [255,255,0]     #yellow
g = [0,255,0]       #green
b = [0,0,255]       #blue
i = [75,0,130]      #indigo
v = [159,0,255]     #violet
e = [0,0,0]         #off?
 
image = [
e,e,e,e,e,e,e,e,    # 1st line
e,e,e,r,r,e,e,e,    # 2nd line
e,r,r,o,o,r,r,e,    # 3rd line
r,o,o,y,y,o,o,r,    # 4th line
o,y,y,g,g,y,y,o,
y,g,g,b,b,g,g,y,
b,b,b,i,i,b,b,b,
b,i,i,v,v,i,i,b     # 8th line
]
 
sh.set_pixels(image)
sleep(1)
sh.set_rotation(90)
sleep(1)
sh.set_rotation(180)
sleep(1)
sh.set_rotation(270)
sleep(1)
sh.set_rotation(0)
