from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random
from kivy.graphics import Color, Rectangle, InstructionGroup
from kivy.core.image import Image
from kivy.graphics.texture import Texture
from kivy.core.window import Window
import math


class Game(Widget):
    def __init__(self):
        super().__init__()
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text'
        )
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.f_w = 10
        self.f_h = 10
        self.input = (False, False, False)
        self.accept = True
        self.dt_count = 0
        # 色情報が入るよ
        self.field = [[None for i in range(self.f_w)] for j in range(self.f_h)]
        self.current = [[None for i in range(5)] for j in range(5)]
        self.cur_x = 0
        self.cur_y = 0
        self.pattern = dict()
        self.pattern[0] = [[2, 4], [2, 3],
                           [2, 2], [2, 1]]
        self.pattern[1] = [[2, 3], [2, 2],
                           [2, 1], [3, 1]]
        self.pattern[2] = [[2, 3], [2, 2],
                           [2, 1], [1, 1]]
        self.pattern[3] = [[2, 3], [2, 2],
                           [1, 2], [1, 1]]
        self.pattern[4] = [[1, 3], [1, 2],
                           [2, 2], [2, 1]]
        self.pattern[5] = [[2, 3], [1, 2],
                           [2, 2], [2, 1]]
        self.pattern[6] = [[2, 2], [2, 1],
                           [3, 2], [3, 1]]

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def set(self):
        self.cur_y = self.f_w - 3
        self.cur_x = 2
        now = math.floor(random.random()*7)
        color = [(1, 0, 0), (1, 0.5, 0), (0, 0, 1),
                 (0, 1, 0), (1, 0, 1), (0.5, 0.5, 1.0),
                 (1, 1, 0)]
        for p in self.pattern[now]:
            self.current[p[0]][p[1]] = color[now]

    def valid(self, down):
        for x_, blocks in enumerate(self.current):
            for y_, b in enumerate(blocks):
                x = x_+self.cur_x
                y = y_+self.cur_y
                if b is not None and y < self.f_h:
                    y_off = 0
                    x_off = 0
                    if down:
                        y_off = -1
                    elif self.input[0]:
                        x_off = -1
                    elif self.input[1]:
                        x_off = 1
                    if (not down and self.input[2] and
                        (x_+self.cur_y < 0 or 4-y_+self.cur_x < 0
                            or 4-y_+self.cur_x > self.f_w-1 or x_+self.cur_y > self.f_h-1
                                or self.field[4-y_+self.cur_x][x_+self.cur_y] is not None)):
                        return False
                    elif (y+y_off < 0 or x+x_off < 0
                            or x+x_off > self.f_w-1
                            or self.field[x+x_off][y+y_off] is not None):
                        return False
        return True

    def move(self, down):
        if down:
            self.cur_y -= 1
        if not down and self.input[0]:
            self.cur_x -= 1
        elif not down and self.input[1]:
            self.cur_x += 1
        elif not down and self.input[2]:
            new_current = [[None for i in range(5)] for j in range(5)]
            for x, blocks in enumerate(self.current):
                for y, b in enumerate(blocks):
                    new_current[4-y][x] = b
            self.current = new_current

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left' and self.accept:
            self.input = (True, False, False)
            self.accept = False
        elif keycode[1] == 'right' and self.accept:
            self.input = (False, True, False)
            self.accept = False
        elif keycode[1] == 'up' and self.accept:
            self.input = (False, False, True)
            self.accept = False

    def _on_keyboard_up(self, scancode, codepoint):
        self.accept = True

    def stop(self):
        for x_, blocks in enumerate(self.current):
            for y_, b in enumerate(blocks):
                x = x_+self.cur_x
                y = y_+self.cur_y
                if b is not None and y < self.f_h:
                    self.field[x][y] = b
                    self.current[x_][y_] = None

    def erase(self):
        for i in range(self.f_h):
            for y in range(self.f_h):
                clear = True
                for x in range(self.f_w):
                    if self.field[x][y] is None:
                        clear = False
                if clear:
                    for y_ in range(y, self.f_h-1):
                        for x_ in range(self.f_w):
                            self.field[x_][y_] = self.field[x_][y_+1]
                    for x_ in range(self.f_w):
                        self.field[x_][self.f_h-1] = None

    def draw(self):
        self.canvas.clear()
        for x_, blocks in enumerate(self.current):
            for y_, b in enumerate(blocks):
                x = x_+self.cur_x
                y = y_+self.cur_y
                if b is not None and y < self.f_h:
                    with self.canvas:
                        Color(*b)
                        Rectangle(pos=(50+x*50, 50+y*50), size=(50, 50))
        for x, blocks in enumerate(self.field):
            for y, b in enumerate(blocks):
                if b is not None:
                    with self.canvas:
                        Color(*b)
                        Rectangle(pos=(50+x*50, 50+y*50), size=(50, 50))

    def update(self, dt):
        self.dt_count += dt
        down = False
        if self.dt_count > 1.0:
            self.dt_count = 0
            down = True
        if self.valid(down):
            self.move(down)
        elif down:
            self.stop()
            self.erase()
            self.set()
        self.draw()
        if self.input[0] or self.input[1] or self.input[2]:
            self.accept = False
            self.input = (False, False, False)


class TetrisApp(App):
    def build(self):
        game = Game()
        game.set()
        Clock.schedule_interval(game.update, 1/60)
        return game


if __name__ == '__main__':
    TetrisApp().run()
