from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random
from kivy.graphics import Color, Ellipse, Line, InstructionGroup
from kivy.core.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class CustomDropDown(DropDown):
    pass


class PoApp(App):
    def build(self):
        w = Widget()
        dropdown = CustomDropDown()
        mainbutton = Button(text='Hello', size_hint=(
            .1, .1), pos_hint={"x": 0.5, "y": 0.5})
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance,
                      x: setattr(mainbutton, 'text', x))
        w.add_widget(dropdown)
        w.add_widget(mainbutton)
        return w


if __name__ == '__main__':
    PoApp().run()
