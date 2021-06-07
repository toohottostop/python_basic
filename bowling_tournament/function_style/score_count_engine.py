def game_score(game_result):
    analized_res = []
    for point in zip(game_result.replace('X', 'X-')[0::2], game_result.replace('X', 'X-')[1::2]):
        analized_res.append(point)
    errors_handler(analized_res)
    points_counter(analized_res)
    if points_counter(analized_res)[1] != 10:
        raise ValueError('Неправильное количество фреймов')
    return points_counter(analized_res)[0]


def errors_handler(analized_res):
    for point in analized_res:
        if point[0].isdigit() and \
           point[1].isdigit() and \
           int(point[0]) + int(point[1]) >= 10:
            raise ValueError('Введено неправильное значение - сумма одного фрейма больше 9 очков')
        elif '0' in point or \
                (not point[0].isalpha and not point[0].isdigit) or \
                (not point[1].isalpha and not point[1].isdigit):
            raise ValueError('Введено неправильное значение')
        elif '/' in point[0]:
            raise ValueError('Spare на первом броске')
        elif 'X' in point[1]:
            raise ValueError('Strike на втором броске')


def points_counter(analized_res):
    total_points = 0
    frames = 0
    for point in analized_res:
        if 'X' in point:
            total_points += 20
        elif '/' in point:
            total_points += 15
        elif point == ('-', '-'):
            total_points += 0
        elif '-' in point:
            if point[0] == point[0].isdigit:
                total_points += int(point[0])
            else:
                total_points += int(point[1])
        else:
            total_points += int(point[0]) + int(point[1])
        frames += 1
    return total_points, frames
