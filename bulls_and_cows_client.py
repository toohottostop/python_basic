from bulls_and_cows_engine import make_new_number, number_check


def check_user_input():
    while True:
        user_input = input('Please enter a four-digit number: ')
        user_input_set = set(user_input)
        if not user_input.isnumeric():
            print('The string does not consist of numbers!')
            continue
        elif user_input[0] == '0':
            print('Number cannot start from zero!')
            continue
        elif len(user_input_set) != 4:
            print('There should be 4 numbers and they should not be repeated!')
            continue
        else:
            break
    return user_input


make_new_number()
tries = 0
while True:
    user_input = check_user_input()
    tries += 1
    number_check(user_input)
    tries += 1
    if number_check(user_input) == 4:
        print('You WIN!', '\nNumber of strokes: ', tries)
        restart = input('Continue? [Y/N]: ')
        if restart in ['Y', 'y']:
            tries = 0
            make_new_number()
            continue
        else:
            break
