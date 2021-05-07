import os


def sort(vol_list):
    filter_zero_volatility = {key: value for key, value in vol_list.items() if value != 0}
    max_volatility = sorted(filter_zero_volatility.items(), key=lambda x: x[1])[-3:]
    min_volatility = sorted(filter_zero_volatility.items(), key=lambda x: x[1])[:3]
    zero_volatility = [key for key, value in vol_list.items() if value == 0]
    print('Max volatility:')
    for i in max_volatility:
        print(f'{i[0]} - {i[1]}%')
    print('Min volatility:')
    for i in min_volatility:
        print(f'{i[0]} - {i[1]}%')
    print('Zero volatility:')
    print(', '.join(zero_volatility))


def path_to_file(path):
    path = os.path.normpath(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(path, file)
