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


class Child(Human):
    def __init__(self, name, home):
        super().__init__(name=name)
        self.house = home
        self.fullness = 10
        self.happiness = 100

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        return super().act()

    def eat(self):
        if self.house.food >= 10:
            print('{} ate'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('There is no food for child, go to store!', color='red')

    def sleep(self):
        cprint('{} sleep'.format(self.name), color='white')
        self.fullness -= 10


class Cat:
    def __init__(self, name, home):
        self.name = name
        self.house = home
        self.fullness = 30

    def __str__(self):
        return 'Im - Cat №{}, fullness {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('Cat №{} RIP'.format(self.name), color='red')
            return True
        elif self.fullness <= 10:
            self.eat()
        dice = randint(1, 2)
        if dice == 1:
            self.sleep()
        elif dice == 2:
            self.soil()

    def eat(self):
        if self.house.cat_food >= 10:
            print('Cat №{} ate'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            print('Cat has no food!')

    def sleep(self):
        cprint('Cat №{} sleep'.format(self.name), color='blue')
        self.fullness -= 10

    def soil(self):
        cprint('Cat №{} scratching wallpapers'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.dirt += 5


class Simulation(House):
    def __init__(self, money_incidents, food_incidents):
        super().__init__()
        self.cats_quantity = 1
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents

    def one_year(self, cats_quantity, salary):
        cats = []
        random_days = []
        for _ in range(self.food_incidents):
            dice = randint(1, 365)
            random_days.append(dice)
        home = House()
        serge = Husband(name='Serega', home=home, salary=salary)
        masha = Wife(name='Masha', home=home)
        kolya = Child(name='Kolya', home=home)
        for name in range(cats_quantity):
            cat = Cat(name=name, home=home)
            cats.append(cat)

        for day in range(1, 366):
            cprint('================== Day {} =================='.format(day), color='red')
            if day in random_days:
                print(f'In day {day} half of the products have expired')
                home.food = home.food // 2
            if serge.act() or masha.act() or kolya.act():
                print(f'With salary of {salary} people can live {day} days')
                return
            for cat in cats:
                if cat.act():
                    print(f'With salary of {salary} cats can live {day} days')
                    return
            home.dirt_in_house()
            cprint(serge, color='cyan')
            cprint(masha, color='cyan')
            cprint(kolya, color='cyan')
            for cat in cats:
                cprint(cat, color='cyan')
            cprint(home, color='cyan')
            if day == 365:
                return day

    def experiment(self, salary):
        for _ in range(1):
            self.one_year(self.cats_quantity, salary)
            if self.one_year(self.cats_quantity, salary) == 365:
                print(f'With salary of {salary}, you can feed {self.cats_quantity} cats')
                self.cats_quantity += 1


if __name__ == '__main__':
    for food_incidents in range(1, 2):
        for money_incidents in range(1, 2):
            life = Simulation(money_incidents, food_incidents)
            for salary in range(500, 1001, 500):
                life.experiment(salary)
