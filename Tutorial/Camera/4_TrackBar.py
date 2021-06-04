import cv2
import numpy as np
CV_WAITKEY_ENTER            = 13
CV_WAITKEY_ESC              = 27
CV_WAITKEY_SPACE            = 32
CV_WAITKEY_TAB              = 9

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('Shape.mp4')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
isOpened = cap.isOpened()

while(1):
    cv2.imshow('image',img)
    if isOpened==True:
        result, frame = cap.read()
        if result==True:
            cv2.imshow('camera', frame)

    # キー入力受付
    key = cv2.waitKey(1)
    # 終了キー（Escで終了）
    if (key == CV_WAITKEY_ESC):
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cap.release()
cv2.destroyAllWindows()