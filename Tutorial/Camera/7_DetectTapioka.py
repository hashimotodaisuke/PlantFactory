import cv2
import numpy
from matplotlib import pyplot


img_bgr = cv2.imread('Tapioka.jpg')
img_bw = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
## 一定の明るさ(この場合は120)より暗い部分のみ残してみる ##
img_mod = numpy.where(img_bw > 120 , 0, img_bw)
cnt_lst, hir_lst = cv2.findContours(numpy.array(img_mod, dtype = numpy.uint8), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in cnt_lst:
    img = cv2.drawContours(img_mod, [cnt], 0, 128, 5)
fig, ax = pyplot.subplots()
ax.imshow(img)
pyplot.text(50, 200, "The number of Tapioka is :" + str(len(cnt_lst)))
pyplot.show()


## カラーで読み込んだ画像をcvtColorを用いてhsvに変更 ##
img_cl = cv2.imread('Tapioka.jpg')
img_hsv = cv2.cvtColor(img_cl, cv2.COLOR_BGR2HSV)
## 赤色の範囲を定義 ##
hsv_min = numpy.array([150,  64,   0])
hsv_max = numpy.array([180, 255, 255])
## 赤色をマスクする ##   
mask = cv2.inRange(img_hsv, hsv_min, hsv_max)
mask = cv2.bitwise_not(mask)
img_hsv = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)
## 背景の黒い部分などを白くする ##
img_hsv[:, :, 2] = numpy.where(img_hsv[:, :, 2] < 10, 255 * numpy.ones_like(img_hsv[:, :, 2]), img_hsv[:, :, 2])
## HSVからBGRを経由して白黒に変更する ##
img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
img_bw  = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
## ごみを取るためのブラシ処理 ##
img_bw_b = cv2.blur(img_bw, (3, 3))
## 暗い部分のみ残してみる ##
img_bw_b = numpy.where(img_bw_b < 90, 255, 0)
cnt_lst, hir_lst = cv2.findContours(numpy.array(img_bw_b, dtype = numpy.uint8), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in cnt_lst:
    img = cv2.drawContours(img_bw_b, [cnt], 0, 128, 5)
fig, ax = pyplot.subplots()
ax.imshow(img)
pyplot.text(50, 200, "The number of Tapioka is :" + str(len(cnt_lst)))
pyplot.show()
