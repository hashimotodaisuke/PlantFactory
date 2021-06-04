import cv2
import numpy
from matplotlib import pyplot


img_bgr = cv2.imread('Tapioka.jpg')
img = cv2.medianBlur(img_bgr,5) #// 平滑化。これがないと誤検出が起こりやすい
img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img_bw,cv2.HOUGH_GRADIENT,1.0,10,
                            param1=100,param2=27,minRadius=1,maxRadius=20)

circles = numpy.uint16(numpy.around(circles))
count = 0
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img_bgr,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img_bgr,(i[0],i[1]),2,(0,0,255),3)
    count = count + 1
img_rbg = img_bgr[:,:,::-1] # BGR -> RBG.   
fig, ax = pyplot.subplots()
ax.imshow(img_rbg)
pyplot.text(50, 200, "The number of Tapioka is :" + str(count))
pyplot.show()
