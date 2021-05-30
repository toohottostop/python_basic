import multiprocessing
from time_track import time_track
from volatility_sort_and_print import *


def volatility_count(file_name):
    ticker = None
    max_price = 0
    min_price = 0

    with open(file_name, 'r', encoding='utf8') as file:
        file.readline()
        for line in file:
            sec_id, trade_time, price, quantity = line[:-1].split(',')
            price = float(price)
            if sec_id != ticker:
                ticker = sec_id
                max_price, min_price = price, price
            elif max_price < price:
                max_price = price
            elif min_price > price:
                min_price = price

    half_sum = (max_price + min_price) / 2
    volatility = round((((max_price - min_price) / half_sum) * 100), 2)

    return ticker, volatility


@time_track
def main(path):
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    vol_list = pool.map(volatility_count, path_to_file(path=path))
    pool.close()
    pool.join()
    sort(dict(vol_list))


if __name__ == '__main__':
    path = 'trades'
    main(path=path)
