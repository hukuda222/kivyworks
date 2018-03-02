from kivy.uix.image import Image
from players import Player


class Chara(Image):
    def __init__(self, src, x, y, w, h):
        super().__init__(source=src)
        self.pos_hint = {'x': x, 'y': y}
        self.size_hint = (w, h)


class Set:
    def __init__(self, charas, text):
        self.charas = charas
        self.text = text


class Data:
    def __init__(self):
        self.players = [Player(), Player(), Player()]
        self.enc_enemys = list()
        self.sets = [Set([Chara("po.png", 0.3, 0.3, 0.2, 0.2)], "asdfg\nefrtg\na"), Set(
            [], "asdfg\nefrtg\na")]
        self.next = 'mapwalk'

    def make_battle(self, enemys):
        self.enc_enemys = enemys
