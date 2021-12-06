#from color-detection-code import color_detected

#Importing Kivy Widgets

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
from kivy.uix.popup import Popup

#Configuration

kivy.require('1.9.0')
Config.set('graphics','resizable', True)

#Framework for Design Layout

class StartingScreen (Screen):
    pass

class RedGridLayoutCombos(Screen):
    pass

class RedFashionCombinations(Screen):
    pass

class GreenGridLayoutCombos(Screen):
    pass

class GreenFashionCombinations(Screen):
    pass

class BlueGridLayoutCombos (Screen):
    pass

class BlueFashionCombinations (Screen):
    pass

class YellowGridLayoutCombos (Screen):
    pass

class YellowFashionCombinations (Screen):
    pass

class VioletGridLayoutCombos (Screen):
    pass

class VioletFashionCombinations (Screen):
    pass

class BlackGridLayoutCombos (Screen):
    pass

class BlackFashionCombinations (Screen):
    pass

class WhiteGridLayoutCombos (Screen):
    pass

class WhiteFashionCombinations (Screen):
    pass

class OrangeGridLayoutCombos (Screen):
    pass

class OrangeFashionCombinations (Screen):
    pass

class WindowManager (ScreenManager):
    pass

#Designate Our .kv design file

kv = Builder.load_file('layouts.kv')

#Building of Main App

class RBGoggles9000App(App):
    def build(self):
        return kv

#Running Code

if __name__ == "__main__":
    RBGoggles9000App().run()



