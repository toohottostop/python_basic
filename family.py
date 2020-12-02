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


class Husband(Human):
    def __init__(self, name, home, salary):
        super().__init__(name=name)
        self.house = home
        self.house.money = salary

    def act(self):
        dice = randint(1, 2)
        if self.house.cat_food < 10:
            self.buy_cat_food()
        elif dice == 1:
            self.gaming()
        elif dice == 2 or self.house.money < 50:
            self.work()
        return super().act()

    def work(self):
        cprint('{} went to work'.format(self.name), color='yellow')
        self.house.money += salary
        self.fullness -= 10
        House.total_money_earn += 1500

    def gaming(self):
        cprint('{} playing World of Tanks'.format(self.name), color='yellow')
        self.fullness -= 10
        self.happiness += 20

    def buy_cat_food(self):
        if self.house.money >= 10:
            cprint("{} bought cat's food".format(self.name), color='yellow')
            self.house.cat_food += 10
            self.house.money -= 10
            self.fullness -= 10
        else:
            cprint('{} out of money!'.format(self.name), color='red')


class Wife(Human):
    total_fur_coat = 0

    def __init__(self, name, home):
        super().__init__(name=name)
        self.house = home

    def act(self):
        dice = randint(1, 2)
        if self.house.dirt > 90:
            self.clean_house()
        elif self.house.food <= 10:
            self.shopping()
        elif dice == 1 and self.house.money > 350:
            self.buy_fur_coat()
        return super().act()

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} went to store'.format(self.name), color='green')
            self.house.food += 1000
            self.fullness -= 10
            self.house.money -= 10
        else:
            cprint('{} out of money!'.format(self.name), color='red')

    def buy_fur_coat(self):
        cprint('{} bought fur coat'.format(self.name), color='green')
        self.house.money -= 350
        self.fullness -= 10
        self.happiness += 60
        Wife.total_fur_coat += 1

    def clean_house(self):
        cprint('{} cleaned the house'.format(self.name), color='green')
        self.house.dirt -= 100
        self.fullness -= 10
