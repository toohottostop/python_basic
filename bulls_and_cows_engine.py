from random import randint

_numbers = ''


def make_new_number():
    global _numbers
    for i, n in enumerate(_numbers):
        _numbers = _numbers.replace(n, '')
    _numbers += str(randint(1, 9))
    while len(_numbers) < 4:
        number = str(randint(0, 9))
        if number not in _numbers:
            _numbers += number
    # print(_numbers)
    return _numbers


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
    if bulls_and_cows['bulls'] != 4:
        print('BULLS - ', bulls_and_cows['bulls'], ', COWS - ', bulls_and_cows['cows'])
    else:
        return bulls_and_cows['bulls']
