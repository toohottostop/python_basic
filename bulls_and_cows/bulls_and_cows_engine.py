from random import randint

NUMBERS = ''
COUNT = 0


def make_new_number():
    global NUMBERS
    NUMBERS += str(randint(1, 9))
    while len(NUMBERS) < 4:
        number = str(randint(0, 9))
        if number not in NUMBERS:
            NUMBERS += number
    return NUMBERS


def number_check(user_input):
    bulls_and_cows = {'bulls': 0, 'cows': 0}
    numbers_list, user_input_list = list(NUMBERS), list(user_input)
    for i, element in enumerate(numbers_list):
        if element in user_input_list:
            if user_input_list[i] == numbers_list[i]:
                bulls_and_cows['bulls'] += 1
                numbers_list[i] = ' '
            else:
                bulls_and_cows['cows'] += 1
                numbers_list[i] = ' '
    return bulls_and_cows['bulls'], bulls_and_cows['cows']


def tries_count():
    global COUNT
    COUNT += 1
    return COUNT


def game_restart():
    global NUMBERS, COUNT
    NUMBERS = ''
    COUNT = 0
    make_new_number()