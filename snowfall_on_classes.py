# -*- coding: utf-8 -*-
import simple_draw as sd
from random import choice


class Snowflake:

    def __init__(self):
        self.y = choice([y_coord for y_coord in range(600, 800, 10)])
        self.x = choice([x_coord for x_coord in range(0, 600)])
        self.flake_size = choice([flake_size_list for flake_size_list in range(10, 50)])

    def clear_previous_picture(self, color):
        sd.start_drawing()
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.flake_size, color=color)
        sd.finish_drawing()

    def move(self):
        self.y -= 10
        delta = sd.random_number(-5, 5)
        self.x += delta

    def draw(self, color):
        sd.start_drawing()
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.flake_size, color=color)
        sd.finish_drawing()

    def can_fall(self):
        if self.y < 20:
            return self.y < 20


def get_flakes(count):
    flakes_list = []
    for _ in range(0, count):
        flakes_list.append(Snowflake())
    return flakes_list


def get_fallen_flakes():
    fallen_flakes_list = []
    for i, snowflake in enumerate(flakes):
        if snowflake.can_fall():
            fallen_flakes_list.append(i)
    return fallen_flakes_list


def append_flakes(count):
    for i in range(0, len(count)):
        flakes.append(Snowflake())


def delete_flakes(count):
    fallen_flakes.reverse()
    for i, snowflake in enumerate(count):
        flakes.pop(snowflake)


N = 20  # Number of flakes

flake = Snowflake()
flakes = get_flakes(count=N)  # create list of objects SnowFlake()

while True:
    for flake in flakes:
        flake.clear_previous_picture(color=sd.background_color)
        flake.move()
        flake.draw(color=sd.COLOR_WHITE)
    fallen_flakes = get_fallen_flakes()  # count how many snowflakes have already fallen
    if fallen_flakes:
        delete_flakes(count=fallen_flakes)
        append_flakes(count=fallen_flakes)  # add more snowflakes on top
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()