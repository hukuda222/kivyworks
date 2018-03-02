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
from kivy.lang import Builder

Builder.load_file('./field.kv')


class Chip(Widget):
    def __init__(self, x, y, color, type_state):
        super().__init__()
        self.ipos[0] = x
        self.ipos[1] = y
        self.color = color
        self.type = type_state


class Field():
    def __init__(self, game, w, h):
        self.w = w
        self.h = h
        self.map = list()
        for ih in range(self.h):
            self.map.append(list())
            for iw in range(self.w):
                if ih == 3 and iw == 2:
                    self.map[ih].append(
                        Chip(ih, iw, (.25, .90, .95), 'obstacle'))
                    game.add_widget(self.map[ih][iw])
                else:
                    self.map[ih].append(Chip(ih, iw, (.25, .50, .25), 'po'))
                    game.add_widget(self.map[ih][iw])
