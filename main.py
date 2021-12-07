#RBGoggles9000
#EG 1003 Fall 2021 Section G3
#Sachi Parikh, Redwan Ramim, Matthew Olmedo, and Diana Solis
#Copyright 2021


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

clr = open("color.txt", "r")
contents = clr.read()

clr.close()

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

class WindowManager (ScreenManager):
    pass

#Designate Our .kv design file

kv = Builder.load_file('layouts.kv')

#Building of Main App

class RBGoggles9000App(App):
    content = StringProperty(contents)
    def build(self):
        return kv

RBGoggles9000App().run()
 
    



