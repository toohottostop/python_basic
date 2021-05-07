import simple_draw as sd
from snowfall import create_snowflakes, snowflakes_color, move_snowflakes, fallen_snowflakes, delete_snowflakes, N

create_snowflakes(N)
while True:
    snowflakes_color(color=sd.background_color)
    move_snowflakes()
    snowflakes_color(color=sd.COLOR_WHITE)
    fallen_snowflakes()
    delete_snowflakes()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
