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
from kivy.uix.image import Image
from kivy.graphics import *
from kivy.uix.label import Label

Builder.load_file('./battle.kv')


class Chara(Image):
    def __init__(self, src, x, y, w, h):
        super().__init__(source=src)
        self.pos_hint = {'x': x, 'y': y}
        self.size_hint = (w, h)


class Battle(Screen):
    def __init__(self, data, scene_name):
        super().__init__(name=scene_name)
        self.data = data
        field = ObjectProperty(None)
        log = ObjectProperty(None)
        self.log.bind(on_touch_down=lambda x, y: self.log_put())

    def log_put(self):
        self.log.text = self.charas[self.act_id].act(
            self.data.players, self.data.enc_enemys)
        self.act_id += 1
        if self.act_id == len(self.charas):
            self.act_id = 0

    def on_enter(self):
        self.players = list()
        self.enemys = list()
        self.text = ""
        self.charas = self.data.players + self.data.enc_enemys
        self.act_id = 0
        for i, p in enumerate(self.data.players):
            self.players.append(
                Chara(p.src, 0.4 + i * 0.2, 0.4, 0.1, 0.1))
            self.field.add_widget(self.players[i])
        for i, e in enumerate(self.data.enc_enemys):
            self.enemys.append(
                Chara(e.src, 0.4 + i * 0.2, 0.8, 0.1, 0.1))
            self.field.add_widget(self.enemys[i])
