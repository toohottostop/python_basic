from volatility_sort_and_print import *
from time_track import time_track


class VolatilityCounter:

    def __init__(self, file_name):
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
def main():
    for file_name in path_to_file(path=path):
        count_volatility = VolatilityCounter(file_name=file_name)
        count_volatility.run()
        vol_list.setdefault(count_volatility.ticker, count_volatility.volatility)


if __name__ == '__main__':
    path = 'trades'
    vol_list = {}
    main()
    sort(vol_list)