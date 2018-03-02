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
from skill import Skill
from kivy.uix.image import Image
from skill import Skill


Builder.load_file('./players.kv')


def handler(func, *args):
    return func(*args)


class Player:
    def __init__(self):
        self.hp = 100
        self.mp = 10  # 魔法パワー
        self.bp = 10  # 物理パワー
        self.guard = False
        self.src = "po.png"
        self.name = "hukuda"

    def act(self, players, enemys):
        self.guard = False
        return handler(Skill["min_attack"], self, players, enemys)


class Players(Widget):
    def __init__(self, x, y):
        super().__init__()
        self.ipos[0] = x
        self.ipos[1] = y
