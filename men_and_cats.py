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


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, fullness {}'.format(
            self.name, self.fullness)

    def pick_cat(self, cat, house):
        self.fullness -= 10
        cat.house = house
        cprint('{} picked cat'.format(self.name), color='cyan')

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} bought food for cats'.format(self.name), color='blue')
            self.house.cat_food += 50
            self.house.money -= 50
        else:
            cprint('{} out of money!'.format(self.name), color='red')

    def house_cleaning(self):
        print('{} cleaned up'.format(self.name))
        self.fullness -= 20
        self.house.dirt -= 100

    def eat(self):
        if self.house.man_food >= 10:
            cprint('{} ate'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.man_food -= 10
        else:
            cprint('{} no food'.format(self.name), color='red')

    def work(self):
        cprint('{} went on work'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} watched MTV all day long'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} went to store'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.man_food += 100
        else:
            cprint('{} spent all money!!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} moved inda house'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} died...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.house.man_food <= 20:
            self.shopping()
        if self.house.cat_food <= 20:
            self.buy_cat_food()
        if self.house.dirt >= 100:
            self.house_cleaning()
        if dice == 1 or self.house.money < 50:
            self.work()
        elif dice == 2 or self.fullness < 30:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.man_food = 50
        self.cat_food = 0
        self.money = 0
        self.dirt = 0

    def __str__(self):
        return 'Food left in the house {}, money left {}, food in cat bowl {}, dirt {}'.format(
            self.man_food, self.money, self.cat_food, self.dirt)


citizens = [
    Man(name='Beavis'),
    Man(name='Butthead'),
    Man(name='Kenny'),
]
cats = [
    Cat(name='Cocos'),
    Cat(name='Missuri'),
    Cat(name='Pussycat'),
]

my_sweet_home = House()
for cat, citizen in zip(cats, citizens):
    citizen.go_to_the_house(house=my_sweet_home)
    citizen.pick_cat(cat, house=my_sweet_home)

for day in range(1, 366):
    print('================ day {} =================='.format(day))
    print('~~Guys~~')
    for citizen in citizens:
        citizen.act()
    print('~~Cats~~')
    for cat in cats:
        cat.act()
    print('--- in the end of the day ---')
    for citizen in citizens:
        print(citizen)
    for cat in cats:
        print(cat)
    print(f'{my_sweet_home}\n')
