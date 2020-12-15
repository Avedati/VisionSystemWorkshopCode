import cv2
cap = cv2.VideoCapture(0)

while True:
	_, picture = cap.read() # read a picture
	
	black_and_white_picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(black_and_white_picture, (3, 3), 0)
	
	cv2.imshow("Video", blurred) # display the picture (optional)
	if cv2.waitKey(1) & 0xFF == 27: # escape key (optional)
		break

cap.release()
cv2.destroyAllWindows()
