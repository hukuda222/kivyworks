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
from kivy.graphics import *
from kivy.uix.label import Label

Builder.load_file('./story.kv')


class Story(Screen):
    def __init__(self, data, scene_name):
        super().__init__(name=scene_name)
        self.data = data
        field = ObjectProperty(None)
        log = ObjectProperty(None)
        self.log.bind(on_touch_down=lambda x, y: self.log_put())

    def update(self, dt):
        if len(self.sets[self.set_id].text) != self.text_id:
            self.text += self.sets[self.set_id].text[self.text_id]
            self.text_id += 1
            self.log.text = self.text

    def log_put(self):
        if len(self.sets[self.set_id].text) != self.text_id:
            self.text = self.sets[self.set_id].text
        elif len(self.sets) - 1 > self.set_id:
            for chara in self.sets[self.set_id].charas:
                self.remove_widget(chara)
            self.text = ""
            self.text_id = 0
            self.set_id += 1
            for chara in self.sets[self.set_id].charas:
                self.add_widget(chara)
        else:
            self.parent.current = self.data.next
        self.log.text = self.text

    def on_enter(self):
        self.sets = self.data.sets
        self.set_id = 0
        self.text = ""
        self.text_id = 0
        for chara in self.sets[0].charas:
            self.add_widget(chara)
        self.event = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def on_leave(self):
        Clock.unschedule(self.event)
