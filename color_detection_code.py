import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import keyboard

color_detected = "0"

while(True):
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 30

    rawCapture = PiRGBArray(camera, size=(640,480))

    for frame in camera.capture_continuous(rawCapture, format = "bgr", use_video_port=True):
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
        
        #Combination of colors
        
        combine_red_green = cv2.bitwise_or(result_red, result_green)
        combine_blue_yellow = cv2.bitwise_or(result_blue, result_yellow)
        combine_white_black = cv2.bitwise_or(result_white, result_black)
        combine_orange_violet = cv2.bitwise_or(result_orange, result_violet)
        combine_rgby = cv2.bitwise_or(combine_red_green, combine_blue_yellow)
        combine_wbov = cv2.bitwise_or(combine_white_black, combine_orange_violet)
        #combine_colors = cv2.bitwise_or(combine_rgby, combine_wbov)
        combine_colors = cv2.bitwise_or(combine_red_green, result_blue) #CODE DETECTS RED BLUE AND GREEN FOR EXAMPLE
        final_resulr = cv2.imshow('combine_colors', combine_colors)
        rawCapture.truncate(0)
        
        #Conditionals for Color Detection
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            camera.close()
            
            if(cv2.countNonZero(red_mask)>0):
                color_detected = "1"
                print(color_detected)
                
            if(cv2.countNonZero(green_mask)>0):
                color_detected = "2"
                print(color_detected)
                
            if(cv2.countNonZero(blue_mask)>0):
                color_detected = "3"
                print(color_detected)
                
            #if(cv2.countNonZero(yellow_mask)>0):
                #color_detected = "4"
                #print(color_detected)
                
            #if(cv2.countNonZero(white_mask)>0):
                #color_detected = "5"
                #print(color_detected)
                
            #if(cv2.countNonZero(black_mask)>0):
                #color_detected = "6"
                #print(color_detected)
                
            #if(cv2.countNonZero(orange_mask)>0):
                #color_detected = "7"
                #print(color_detected)
                
            #if(cv2.countNonZero(violet_mask)>0):
                #color_detected = "8"
                #print(color_detected)
                
                #Conditional Statements 4-6 Commented Out For Purpose of RGB Color Detection for Demonstration
                
                
            file = open("color.txt", "w")
            file.write(color_detected)
            file.close
            break
            


