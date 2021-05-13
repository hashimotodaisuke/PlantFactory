import cv2

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
			# キー入力受付
			key = cv2.waitKey(1)
			# 終了キー（EnterかEscで終了）
			if (key == 13) or (key == 27):
				break
cap.release()
cv2.destroyAllWindows()
