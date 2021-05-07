import threading

from python_multiprocessing_and_multithreading.time_track import time_track
from python_multiprocessing_and_multithreading.volatility_sort_and_print import sort, path_to_file


class VolatilityCounter(threading.Thread):
    def __init__(self, file_name, *args, **kwargs):
        threading.Thread.__init__(self,  *args, **kwargs)
        self.file_name = file_name
        self.ticker = None
        self.max_price = 0
        self.min_price = 0
        self.volatility = 0

    def run(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            self.get_max_and_min_price(file=file)
            self.volatility_count()

    def get_max_and_min_price(self, file):
        file.readline()
        for line in file:
            sec_id, trade_time, price, quantity = line[:-1].split(',')
            price = float(price)
            if sec_id != self.ticker:
                self.ticker = sec_id
                self.max_price, self.min_price = price, price
            elif self.max_price < price:
                self.max_price = price
            elif self.min_price > price:
                self.min_price = price

    def volatility_count(self):
        half_sum = (self.max_price + self.min_price) / 2
        self.volatility = round((((self.max_price - self.min_price) / half_sum) * 100), 2)


@time_track
def main(path, vol_list):
    volatility_counters = [VolatilityCounter(file_name=file_name) for file_name in path_to_file(path=path)]
    for counter in volatility_counters:
        counter.start()
    for counter in volatility_counters:
        counter.join()
        vol_list.setdefault(counter.ticker, counter.volatility)


if __name__ == '__main__':
    path = 'trades'
    vol_list = {}
    main(path=path, vol_list=vol_list)
    sort(vol_list)
