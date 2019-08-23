import cv2
import numpy



#camera_active = True
vc = cv2.VideoCapture(0)
firstFrame = None
count = 0




ret, frame = vc.read()
ret, frame1 = vc.read()





while (1):
	#(grabed, frame) = vc.read()
	diff = cv2.absdiff(frame, frame1)
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	i, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	dilated  = cv2.dilate(thresh, None, iterations = 3)
	contours, i = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for contour in contours:
		(x, y, w, h) = cv2.boundingRect(contour)

		if cv2.contourArea(contour) < 900:
			continue
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		cv2.putText(frame, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3) 
	cv2.putText(frame, "Version: {}".format('Alpha 0.2'), (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.66, (0, 255, 0), 2)

	
	cv2.imshow ("Eye", frame)
	frame = frame1
	stream_key = cv2.waitKey(1)
	ret, frame1 = vc.read()

	if stream_key == 27:
		break
