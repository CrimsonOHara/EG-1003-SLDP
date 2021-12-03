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
        #red
		red_lower = np.array([160,70,50])
		red_upper = np.array([180,255,255])
		red_mask = cv2.inRange(hsv,red_lower,red_upper)
		result_red = cv2.bitwise_and(frame,frame,mask=red_mask)
        #green
		green_lower = np.array([40,40,40])
		green_upper = np.array([102,255,255])
		green_mask = cv2.inRange(hsv,green_lower,green_upper)
		result_green = cv2.bitwise_and(frame, frame, mask = green_mask)
        #blue
        blue_lower = np.array([90,50,50])
        blue_upper = np.array([130,255,255])
        blue_mask = cv2.inRange(hsv,blue_lower,blue_upper)
        result_blue = cv2.bitwise_and(frame, frame, mask = blue_mask)
        #yellow
        yellow_lower = np.array([20,100,100])
        yellow_upper = np.array([30,255,255])
        yellow_mask = cv2.inRange(hsv,yellow_lower,yellow_upper)
        result_yellow = cv2.bitwise_and(frame, frame, mask = yellow_mask)
        #white
        sensitivity = 15
        white_lower = np.array([0,0,255-sensitivity])
        white_upper = np.array([255,sensitivity,255])
        white_mask = cv2.inRange(hsv,white_lower,white_upper)
        result_white = cv2.bitwise_and(frame, frame, mask = white_mask)
        #black
        black_lower = np.array([0,0,0])
        black_upper = np.array([180,255,46])
        black_mask = cv2.inRange(hsv,black_lower,black_upper)
        result_black = cv2.bitwise_and(frame, frame, mask = black_mask)
        #orange
        orange_lower = np.array([0,160,40])
        orange_upper = np.array([17,255,255])
        orange_mask = cv2.inRange(hsv,orange_lower,orange_upper)
        result_orange = cv2.bitwise_and(frame, frame, mask = orange_mask)
        #violet
        violet_lower = np.array([135,160,60])
        violet_upper = np.array([155,255,255])
        violet_mask = cv2.inRange(hsv,violet_lower,violet_upper)
        result_violet = cv2.bitwise_and(frame, frame, mask = violet_mask)
        
	    combine_colors = cv2.bitwise_or(result_red, result_green, result_blue, result_yellow, result_white, result_black, result_orange, result_violet)
		final_resulr = cv2.imshow('combine_colors', combine_colors)
		rawCapture.truncate(0)
		
		if cv2.waitKey(10) & 0xFF == ord('q'):
    			camera.close()
			if(cv2.countNonZero(red_mask)>0):
				print('Detected red. Color Wheel:')
				print('Complimetary color is green. Triadactic colors are blue and yellow. Tetradic colors are blue, red, and orange.')
			if(cv2.countNonZero(green_mask)>0):
				print('Detected green. Color Wheel:')
				print('Complimetary color is red. Triadactic colors are purple and  orange. Tetradic colors are blue, green, and orange.')
			if(cv2.countNonZero(blue_mask)>0):
				print('Detected blue. Color Wheel:')
			if(cv2.countNonZero(yellow_mask)>0):
				print('Detected yellow. Color Wheel:')
			if(cv2.countNonZero(white_mask)>0):
				print('Detected white.')
			if(cv2.countNonZero(black_mask)>0):
				print('Detected black.')
			if(cv2.countNonZero(orange_mask)>0):
				print('Detected orange.')
			if(cv2.countNonZero(violet_mask)>0):
				print('Detected violet.')
				break