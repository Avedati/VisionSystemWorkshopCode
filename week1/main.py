import cv2
cap = cv2.VideoCapture(0)

while True:
	_, picture = cap.read() # read a picture
	# do some stuff
	cv2.imshow("Video", picture) # display the picture (optional)
	if cv2.waitKey(1) & 0xFF == 27: # escape key (optional)
		break

cap.release()
cv2.destroyAllWindows()
