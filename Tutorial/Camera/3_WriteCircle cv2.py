import cv2
import numpy as np

CV_WAITKEY_ENTER            = 13
CV_WAITKEY_ESC              = 27
CV_WAITKEY_SPACE            = 32
CV_WAITKEY_TAB              = 9

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        # cv2.rectangle(img,(x,y),(x+50, y+100),(0,0,255),0)
        # cv2.line(img, (x, y), (x+50, y), (0, 255, 0), thickness=1, lineType=cv2.LINE_4)
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    # キー入力受付
    key = cv2.waitKey(1)
    # 終了キー（Escで終了）
    if (key == CV_WAITKEY_ESC):
        break
cv2.destroyAllWindows()