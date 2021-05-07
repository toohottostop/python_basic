import simple_draw as sd

N = 20  # number of snowflakes
y_coord = []  # list of y coordinates of snowflakes
x_coord = []  # list of x coordinates of snowflakes
flake_size_list = []  # list of ray lengths of snowflakes
fallen_flakes_list = []


def create_snowflakes(N):
    for i in range(N):
        y_coord.append(sd.random_number(600, 900))
        x_coord.append(sd.random_number(50, 550))
        flake_size_list.append(sd.random_number(10, 50))


def snowflakes_color(color):
    sd.start_drawing()
    for i, y in enumerate(y_coord):
        point = sd.get_point(x_coord[i], y_coord[i])
        sd.snowflake(center=point, length=flake_size_list[i], color=color)
    sd.finish_drawing()


def move_snowflakes():
    for i, y in enumerate(y_coord):
        y_coord[i] -= 10
        delta = sd.random_number(-5, 5)
        x_coord[i] += delta


def fallen_snowflakes():
    for i, y in enumerate(y_coord):
        if y_coord[i] < 20:
            fallen_flakes_list.append(i)
    N = len(fallen_flakes_list)
    return create_snowflakes(N)


def delete_snowflakes():
    global fallen_flakes_list
    fallen_flakes_list.reverse()
    for i, y in enumerate(fallen_flakes_list):
        y_coord.pop(y)
        x_coord.pop(y)
        flake_size_list.pop(y)
    fallen_flakes_list = []
