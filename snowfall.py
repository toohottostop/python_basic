import simple_draw as sd


def snowflake(x, y, size, color):
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=size, color=color)


N = 20  # number of snowflakes
y_coord = []
x_coord = []
flake_size_list = []
for _ in range(N):
    y_coord.append(sd.random_number(600, 900))
    x_coord.append(sd.random_number(50, 550))
    flake_size_list.append(sd.random_number(10, 50))

while True:
    sd.start_drawing()
    for i, y in enumerate(y_coord):
        delta = sd.random_number(-5, 5)
        snowflake(x=x_coord[i], y=y_coord[i], size=flake_size_list[i], color=sd.background_color)
        y_coord[i] -= 10
        x_coord[i] += delta
        snowflake(x=x_coord[i], y=y_coord[i], size=flake_size_list[i], color=sd.COLOR_WHITE)
        if y_coord[i] < 20:
            y_coord[i] = y_coord.index(y_coord[i])
            y_coord[i] = sd.random_number(600, 900)
    sd.finish_drawing()
    sd.sleep(0.1)

    if sd.user_want_exit():
        break

sd.pause()
