import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.utils import get_color_from_hex
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.image import AsyncImage
from kivy.properties import StringProperty
from kivy.core.window import Window

kivy.require('1.9.0')
Config.set('graphics','resizable', True)

#Framework for Design Layout

class CamApp (App):

    def build(self):
        while True:
            camera = PiCamera()
            camera.resolution = (640, 480)
            camera.framerate = 30

        rawCapture = PiRGBArray(camera, size=(640, 480))

        for frame in camera.capture_continuous(rawCapture, formate="bgr", use_video_port=True):
            frame = frame.array
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            red_lower = np.array([160, 70, 50])
            red_upper = np.array([180, 255, 255])
            red_mask = cv2.inRange(hsv, red_lower, red_upper)
            result_red = cv2.bitwise_and(frame, frame, mask=red_mask)

            green_lower = np.array([40, 40, 40])
            green_upper = np.array([102, 255, 255])
            green_mask = cv2.inRange(hsv, green_lower, green_upper)
            result_green = cv2.bitwise_and(frame, frame, mask=green_mask)

            combine_red_green = cv2.bitwise_or(result_red, result_green)
            final_resulr = cv2.imshow('combine_red_green', combine_red_green)
            rawCapture.truncate(0)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            camera.close()
            if (cv2.countNonZero(red_mask) > 0):
                print('Detected red. Color Wheel:')
                print('Complimetary color is green. Triadactic colors are blue and yellow. Tetradic colors are blue, red, and orange.')

            if (cv2.countNonZero(green_mask) > 0):
                print('Detected green. Color Wheel:')
                print('Complimetary color is red.Triadactic colors are purple and orange.Tetradic colors are blue, green, and orange.')
                print('--------------------------')

class RedGridLayoutCombos(Screen):
    pass

class RedFashionCombinations(Screen):
    pass

class WindowManager (ScreenManager):
    pass

#Designate Our .kv design file

kv = Builder.load_file('picamera.kv')

#Building of Main App

class RBGoggles9000App(App):
    def build(self):
        return kv

#Running Code

if __name__ == "__main__":
    RBGoggles9000App().run()



