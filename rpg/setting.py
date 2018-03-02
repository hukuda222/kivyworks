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

Builder.load_file('./setting.kv')

koho = ["自分が中破", "仲間が中破", "自分が瀕死", "仲間が瀕死",
        "敵が中破", "敵が瀕死", "敵が複数", "敵は一体"]


class Setting(Screen):
    def __init__(self, data, scene_name):
        super().__init__(name=scene_name)
        self.select = {"cond0": -1, "cond1": -1}
        self.data = data
        cond = [DropDown(), DropDown()]
        for j, cond_id in enumerate(["cond0", "cond1"]):
            setattr(cond[j], 'triger_id', cond_id)
            for i, k in enumerate(koho):
                btn = Button(text=k, height=30, size_hint_y=None)
                setattr(btn, 'select_id', i)
                setattr(btn, 'dropdown', cond[j])
                btn.bind(on_release=lambda btn: self.btn_dropdown(btn))
                cond[j].add_widget(btn)
            self.ids[cond[j].triger_id].bind(on_release=cond[j].open)
            cond[j].bind(on_select=lambda instance,
                         x: setattr(self.ids[instance.triger_id], 'text', x))

    def btn_dropdown(self, btn):
        btn.dropdown.select(btn.text)
        self.select[btn.dropdown.triger_id] = btn.select_id

    def put(self, score):
        print(score)
