from bulls_and_cows_engine import make_new_number, number_check, tries_count, game_restart


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
while True:
    user_input = check_user_input()
    count = tries_count()
    print('BULLS - ', number_check(user_input)[0], ', COWS - ', number_check(user_input)[1])
    if number_check(user_input)[0] == 4:
        print('You WIN!', '\nNumber of strokes: ', count)
        restart = input('Continue? [Y/N]: ')
        if restart in ['Y', 'y']:
            game_restart()
            continue
        else:
            break
