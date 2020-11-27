from termcolor import cprint
from random import randint


class House:
    total_money_earn = 0
    total_food_eaten = 0

    def __init__(self):
        self.money = 1000
        self.food = 500
        self.dirt = 0
        self.cat_food = 300

    def __str__(self):
        return 'Food left in the house {}, money left {}, dirt {}'.format(
            self.food, self.money, self.dirt)

    def dirt_in_house(self):
        self.dirt += 5


class Human:

    def __init__(self, name):
        self.name = name
        self.fullness = 300
        self.happiness = 100
        self.house = None

    def __str__(self):
        return 'Я - {}, fullness {}, happiness {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        if self.happiness <= 10 or self.fullness <= 0:
            cprint('{} RIP'.format(self.name), color='red')
            return True
        elif self.fullness <= 10:
            self.eat()
        dice = randint(1, 2)
        if self.house.dirt > 90:
            self.happiness -= 10
        elif dice == 1:
            self.stroke_cat()

    def eat(self):
        if self.house.food >= 10:
            print('{} ate'.format(self.name))
            self.fullness += 300
            self.house.food -= 10
            House.total_food_eaten += self.house.food
        else:
            print('There is no food in the house, you need to go to the store!')

    def stroke_cat(self):
        cprint('{} stroked cat'.format(self.name), color='magenta')
        self.happiness += 5
