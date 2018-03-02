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
import mapwalk
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import setting
import title
import battle
import data
import story
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path('./src/fonts')
LabelBase.register(DEFAULT_FONT, 'TakaoPGothic.ttf')
resource_add_path('./src/img')


class RpgApp(App):
    def build(self):
        self.title = 'RPG'
        self.data = data.Data()
        sm = ScreenManager()
        sm.add_widget(setting.Setting(self.data, scene_name='setting'))
        sm.add_widget(mapwalk.MapWalk(self.data, scene_name='mapwalk'))
        sm.add_widget(story.Story(self.data, scene_name='story'))
        sm.add_widget(battle.Battle(self.data, scene_name='battle'))
        sm.add_widget(title.Title(scene_name='title'))

        return sm


if __name__ == '__main__':
    RpgApp().run()
