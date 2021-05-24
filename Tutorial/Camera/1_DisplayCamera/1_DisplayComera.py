import cv2
CV_WAITKEY_ENTER            = 13
CV_WAITKEY_ESC              = 27
CV_WAITKEY_SPACE            = 32
CV_WAITKEY_TAB              = 9

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
isOpened = cap.isOpened()
if isOpened==True:
	while True:
		result, frame = cap.read()
		if result==True:
			# 画像表示
			cv2.imshow('camera', frame)
			# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			# cv2.imshow('camera', gray)
			# キー入力受付
			key = cv2.waitKey(1)
			# 終了キー（Escで終了）
			if (key == CV_WAITKEY_ESC):
				break
cap.release()
cv2.destroyAllWindows()
