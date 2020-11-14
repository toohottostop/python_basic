# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return 'Kitten - {}, fullness {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} ate'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('Kittens dont have food', color='red')

    def sleep(self):
        cprint('{} slept'.format(self.name), color='white')
        self.fullness -= 10

    def wallpaper(self):
        cprint('{} strip off wallpapers'.format(self.name), color='magenta')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} dead...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness <= 20:
            self.eat()
        if dice == 1:
            self.sleep()
        elif dice == 2:
            self.wallpaper()
