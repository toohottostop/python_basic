import multiprocessing
from time_track import time_track
from volatility_sort_and_print import *


class VolatilityCounter(multiprocessing.Process):
    def __init__(self, file_name, conn, *args, **kwargs):
        multiprocessing.Process.__init__(self, *args, **kwargs)
        self.file_name = file_name
        self.ticker = None
        self.max_price = 0
        self.min_price = 0
        self.volatility = 0
        self.conn = conn

    def run(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            self.get_max_and_min_price(file=file)
            self.volatility_count()
        self.conn.send([self.ticker, self.volatility])
        self.conn.close()

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
    volatility_counters, pipes = [], []
    for file_name in path_to_file(path=path):
        parent_conn, child_conn = multiprocessing.Pipe()
        counter = VolatilityCounter(file_name=file_name, conn=child_conn)
        volatility_counters.append(counter)
        pipes.append(parent_conn)
    for counter in volatility_counters:
        counter.start()
    for conn in pipes:
        ticker, volatility = conn.recv()
        vol_list.setdefault(ticker, volatility)
    for counter in volatility_counters:
        counter.join()


if __name__ == '__main__':
    path = 'trades'
    vol_list = {}
    main(path=path, vol_list=vol_list)
    sort(vol_list)
