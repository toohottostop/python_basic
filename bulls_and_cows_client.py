from bulls_and_cows_engine import _numbers, make_number, number_check

make_number()
tries = 0
user_input = None
while user_input != _numbers:
    user_input = input('Please enter a four-digit number: ')
    number_check(user_input)
    tries += 1
    if user_input == _numbers:
        print('You WIN!', '\nNumber of strokes: ', tries)
        restart = input('Continue? [Y/N]: ')
        if restart in ['Y', 'y']:
            _numbers = ''
            make_number()
            continue
        else:
            break
