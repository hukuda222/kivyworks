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


class Block(Widget):
    def __init__(self, i, j):
        super().__init__()
        self.ans = i
        self.now = j


class Game(Widget):
    def set(self):
        self.blocks = list()
        self.now_move = -1
        ran = [i for i in range(16)]
        random.shuffle(ran)
        for i in range(16):
            self.blocks.append(Block(i, ran[i]))
            self.add_widget(self.blocks[i])

    def on_touch_move(self, touch):
        for block in self.blocks:
            if block.collide_point(touch.x, touch.y):
                if block.ans != 15:
                    self.now_move = block.ans
                elif self.now_move != -1:
                    old_pos = block.now
                    block.now = self.blocks[self.now_move].now
                    self.blocks[self.now_move].now = old_pos


class PuzzleApp(App):
    def build(self):
        game = Game()
        game.set()
        return game


if __name__ == '__main__':
    PuzzleApp().run()
