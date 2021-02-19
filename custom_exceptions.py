import random
from termcolor import cprint


class CustomError(Exception):
    pass


class IamGodError(CustomError):
    pass


class DrunkError(CustomError):
    pass


class CarCrashError(CustomError):
    pass


class GluttonyError(CustomError):
    pass


class DepressionError(CustomError):
    pass


class SuicideError(CustomError):
    pass


def one_day():
    dice = random.randint(1, 13)
    if dice != 13:
        current_carma = random.randint(1, 7)
        return current_carma
    else:
        raise CustomError


ENLIGHTENMENT_CARMA_LEVEL = 777
current_carma = 0
day = 0
errors = [IamGodError('Hero GOD'),
          DrunkError('Hero drunk'),
          CarCrashError('Hero crashed in car'),
          GluttonyError('Hero overeating'),
          DepressionError('Hero in depression'),
          SuicideError('Hero self-destructed')]

while current_carma <= ENLIGHTENMENT_CARMA_LEVEL:
    try:
        current_carma += one_day()
    except CustomError:
        cprint(f'Error: {random.choice(errors)}', color='red')
    day += 1
    print(f'Сurrent amount of karma: {current_carma}')
cprint(f'It took the hero {day} days to enlighten', color='green')
