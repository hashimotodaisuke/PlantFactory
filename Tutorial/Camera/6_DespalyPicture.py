import cv2
import numpy
from matplotlib import pyplot


img_bgr = cv2.imread('Tapioka.jpg')
fig, ax = pyplot.subplots()
ax.imshow(img_bgr)
pyplot.show()


img_bgr = cv2.imread('Tapioka.jpg')
# print(img_bgr.shape) -> (400, 291, 3)
# (400, 291, 3) means (w,h) = (291,400) pixel with 3 bgr
img_rbg = img_bgr[:,:,::-1] #  "::-1" means 123 -> 321, so BGR -> RBG.
fig, ax = pyplot.subplots()
ax.imshow(img_rbg)
pyplot.show()


img_bgr = cv2.imread('Tapioka.jpg')
img_bw = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
fig, ax = pyplot.subplots()
ax.imshow(img_bw)
pyplot.show()


img_bgr = cv2.imread('Tapioka.jpg')
img_bw = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
## 一定の明るさ(この場合は120)より暗い部分のみ残してみる ##
img_mod = numpy.where(img_bw > 120 , 0, img_bw)
fig, ax = pyplot.subplots()
ax.imshow(img_mod)
pyplot.show()

