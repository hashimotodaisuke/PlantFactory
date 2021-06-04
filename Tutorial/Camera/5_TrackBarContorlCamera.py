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
cv2.createTrackbar('H','image',0,359,nothing) # 色相(Hue)
cv2.createTrackbar('S','image',0,100,nothing) # 彩度(Saturation・Chroma) 
cv2.createTrackbar('V','image',0,100,nothing) # 明度(Value・Brightness)

cv2.setTrackbarPos('H','image',0)
cv2.setTrackbarPos('S','image',100) 
cv2.setTrackbarPos('V','image',100)

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('Shape.mp4')
isOpened = cap.isOpened()

while(1):
    if isOpened==True:
        result, frame = cap.read()
        if result==True:
            # get current positions of 3 trackbars
            h = cv2.getTrackbarPos('H','image')
            s = cv2.getTrackbarPos('S','image')
            v = cv2.getTrackbarPos('V','image')

            frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # 色空間をBGRからHSVに変換

            frame_hsv[:,:,(0)] = frame_hsv[:,:,(0)]+h # 色相の計算
            frame_hsv[:,:,(1)] = frame_hsv[:,:,(1)]*(s/100) # 彩度の計算
            frame_hsv[:,:,(2)] = frame_hsv[:,:,(2)]*(v/100) # 明度の計算
            frame_bgr = cv2.cvtColor(frame_hsv,cv2.COLOR_HSV2BGR) # 色空間をHSVからBGRに変換

            cv2.imshow('image', frame_bgr)

    # キー入力受付
    key = cv2.waitKey(1)
    # 終了キー（Escで終了）
    if (key == CV_WAITKEY_ESC):
        break

cap.release()
cv2.destroyAllWindows()