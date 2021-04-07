import os


class VolatilityCounter:

    def __init__(self, path):
        self.path = os.path.normpath(path)
        self.price_and_volatility = {}

    def run(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                with open(os.path.join(self.path, file), 'r', encoding='utf8') as ff:
                    self.get_max_and_min_price(ff=ff)
        return self.sort()

    def get_max_and_min_price(self, ff):
        ff.readline()
        for line in ff:
            sec_id, trade_time, price, quantity = line[:-1].split(',')
            price = float(price)
            if sec_id not in self.price_and_volatility:
                ticker_price = self.price_and_volatility.setdefault(sec_id, {'max': price, 'min': price})
            elif ticker_price['max'] < price:
                ticker_price['max'] = price
            elif ticker_price['min'] > price:
                ticker_price['min'] = price
        self.volatility_count(sec_id=sec_id)

    def volatility_count(self, sec_id):
        max_price = self.price_and_volatility[sec_id]['max']
        min_price = self.price_and_volatility[sec_id]['min']
        half_sum = (max_price + min_price) / 2
        self.price_and_volatility[sec_id]['volatility'] = round((((max_price - min_price) / half_sum) * 100), 2)

    def sort(self):
        pass


class MaxVolatility(VolatilityCounter):

    def filter_zero_volatility(self):
        return {key: value for key, value in self.price_and_volatility.items() if value['volatility'] != 0}

    def sort(self):
        filter_zero_volatility = self.filter_zero_volatility()
        return sorted(filter_zero_volatility.items(), key=lambda x: x[1]['volatility'])[-3:]


class MinVolatility(VolatilityCounter):

    def filter_zero_volatility(self):
        return {key: value for key, value in self.price_and_volatility.items() if value['volatility'] != 0}

    def sort(self):
        filter_zero_volatility = self.filter_zero_volatility()
        return sorted(filter_zero_volatility.items(), key=lambda x: x[1]['volatility'])[:3]


class ZeroVolatility(VolatilityCounter):

    def sort(self):
        return [key for key, value in self.price_and_volatility.items() if value['volatility'] == 0]


max_volatility = MaxVolatility(path='trades')
min_volatility = MinVolatility(path='trades')
zero_volatility = ZeroVolatility(path='trades')

print('Максимальная волатильность:')
for i in max_volatility.run():
    print(f'{i[0]} - {i[1]["volatility"]}%')
print('Минимальная волатильность:')
for i in min_volatility.run():
    print(f'{i[0]} - {i[1]["volatility"]}%')
print('Нулевая волатильность:')
print(', '.join(zero_volatility.run()))