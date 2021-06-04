import cv2
CV_WAITKEY_ENTER            = 13
CV_WAITKEY_ESC              = 27
CV_WAITKEY_SPACE            = 32
CV_WAITKEY_TAB              = 9

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('Shape.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        # キー入力受付
        key = cv2.waitKey(1)
        # 終了キー（Escで終了）
        if (key == CV_WAITKEY_ESC):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
