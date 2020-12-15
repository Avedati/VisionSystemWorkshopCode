import cv2
import numpy as np
cap = cv2.VideoCapture(0)

def coerceIntoTape(polygon):
	# TODO: this
	return False

def coerceIntoHexagon(polygon):
	# TODO: this
	return False

while True:
	_, picture = cap.read()
	gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
	gaussian = cv2.GaussianBlur(gray, ksize=(5,5), sigmaX=0)
	canny = cv2.Canny(gaussian, 80, 160)

	kernel = np.ones((15, 15), 'uint8')
	dilated = cv2.dilate(canny, kernel, iterations=1)
	eroded = cv2.erode(dilated, kernel, iterations=1)

	contours, hierarchy = cv2.findContours(eroded, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

	polygons = [cv2.approxPolyDP(c, 0.005 * cv2.arcLength(c, True), True) for c in contours]

	polygons = [p for p in polygons if len(p) < 20]
	polygons = [p for p in polygons if cv2.arcLength(p, False) > 400]

	for p in polygons:
		object_type = None
		if coerceIntoTape(p):
			object_type = 'tape'
		elif coerceIntoHexagon(p):
			object_type = 'hexagon'
		if object_type is not None:
			# TODO: do something with our object
			pass

	# optional stuff
	cv2.drawContours(picture, contours, -1, (0, 255, 0), 2)
	cv2.imshow("contours", picture) # display the picture (optional)
	if cv2.waitKey(1) & 0xFF == 27: # escape key (optional)
		break
