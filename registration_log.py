class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check_log(line):
    if len(line.split(' ')) != 3:
        raise ValueError('Not all fields filled')
    else:
        name, email, age = line.split(' ')
        if not name.isalpha():
            raise NotNameError('Name contain not only letters')
        elif not ('@' in email and '.' in email):
            raise NotEmailError('Invalid email')
        elif not 10 <= int(age) <= 99:
            raise ValueError('Invalid age')


with open('files/registrations.txt', 'r', encoding='utf8') as file:
    with open('files/registrations_good.log', 'w', encoding='utf8') as reg_good, \
            open('files/registrations_bad.log', 'w', encoding='utf8') as reg_bad:
        for line in file:
            line = line[:-1]
            try:
                check_log(line)
            except (ValueError, NotNameError, NotEmailError) as exc:
                if 'unpack' in exc.args[0]:
                    reg_bad.write(f'Not all fields are filled {exc} in line: {line}\n')
                else:
                    reg_bad.write(f'{exc} in line: {line}\n')
            else:
                reg_good.write(f'{line}\n')
