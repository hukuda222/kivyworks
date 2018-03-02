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

Builder.load_file('./enemy.kv')


def handler(func, *args):
    return func(*args)


class Enemy(Widget):
    def __init__(self, x, y, hp, mp, bp, src, name):
        super().__init__()
        self.ipos[0] = x
        self.ipos[1] = y
        self.hp = hp
        self.mp = mp  # 魔法パワー
        self.bp = bp  # 物理パワー
        self.guard = False
        self.src = src
        self.name = name

    def act(self, players, enemys):
        self.guard = False
        if self.name == "スライム":
            return handler(Skill["max_attack"], self, enemys, players)
