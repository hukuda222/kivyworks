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
import field
import players
import enemy
from kivy.uix.screenmanager import ScreenManager, Screen
from general import a_star


class MapWalk(Screen):
    def __init__(self, data, scene_name):
        super().__init__(name=scene_name)
        self.data = data
        self.dir = 0  # 0~3
        self.base = Widget()
        self.add_widget(self.base)
        self.field = field.Field(self.base, 8, 8)
        self.player = players.Players(2, 2)
        self.base.add_widget(self.player)

        self.enemy = enemy.Enemy(4, 4, 30, 5, 5, "po.png", "スライム")
        self.base.add_widget(self.enemy)
        self.move_list = list()

    def on_enter(self):
        self.event = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def on_leave(self):
        Clock.unschedule(self.event)

    def update(self, dt):
        if self.player.collide_point(self.enemy.center_x, self.enemy.center_y):
            self.data.make_battle([self.enemy])
            self.parent.current = 'battle'

        if len(self.move_list) > 0:
            next_move = self.move_list.pop(0)
            if next_move == 0:
                self.player.ipos[1] += 1
            elif next_move == 1:
                self.player.ipos[1] -= 1
            elif next_move == 2:
                self.player.ipos[0] += 1
            elif next_move == 3:
                self.player.ipos[0] -= 1
            self.dir = next_move

    def on_touch_down(self, touch):
        for fl in self.field.map:
            for chip in fl:
                if chip.collide_point(touch.x, touch.y):
                    self.move_list = a_star(
                        self.field.map, self.player.ipos[1], self.player.ipos[0], chip.ipos[1], chip.ipos[0])
