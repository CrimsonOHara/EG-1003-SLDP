import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera

while(True):
	camera = PiCamera()
	camera.resolution = (640,480)
	camera.framerate = 30

	rawCapture = PiRGBArray(camera, size=(640,480))

	for frame in camera.capture_continuous(rawCapture, formate = "bgr", use_video_port=True):
		frame = frame.array
		hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		red_lower = np.array([160,70,50])
		red_upper = np.array([180,255,255])
		red_mask = cv2.inRange(hsv,red_lower,red_upper)
		result_red = cv2.bitwise_and(frame,frame,mask=red_mask)

		green_lower = np.array([40,40,40])
		green_upper = np.array([102,255,255])
		green_mask = cv2.inRange(hsv,green_lower,green_upper)
		result_green = cv2.bitwise_and(frame, frame, mask = green_mask)

		combine_red_green = cv2.bitwise_or(result_red, result_green)
		final_resulr = cv2.imshow('combine_red_green', combine_red_green)
		rawCapture.truncate(0)
		
		if cv2.waitKey(10) & 0xFF == ord('q'):
			camera.close()
			if(cv2.countNonZero(red_mask)>0):
				print('Detected red. Color Wheel:')
				print('Complimetary color is green. Triadactic colors are blue and yellow. Tetradic colors are blue, red, and orange.')
			if(cv2.countNonZero(green_mask)>0):
				print('Detected green. Color Wheel:')
				print(Complimetary color is red. Triadactic colors are purple and and orange. Tetradic colors are blue, green, and orange.')
				print('--------------------------')
				break


