from random import randint

_numbers = ''


def make_number():
    global _numbers
    for _ in range(0, 4):
        _numbers += str(randint(0, 9))
    if _numbers[0] == '0':
        _numbers = _numbers.replace('0', str(randint(1, 9)))


def number_check(user_input):
    bulls_and_cows = {'bulls': 0, 'cows': 0}
    numbers_list, user_input_list = list(_numbers), list(user_input)
    for i, element in enumerate(numbers_list):
        if element in user_input_list:
            if user_input_list[i] == numbers_list[i]:
                bulls_and_cows['bulls'] += 1
                numbers_list[i] = ' '
            else:
                bulls_and_cows['cows'] += 1
                numbers_list[i] = ' '
    print('BULLS - ', bulls_and_cows['bulls'], ', COWS - ', bulls_and_cows['cows'])
