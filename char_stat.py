from pprint import pprint
import zipfile


class Statistics:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.sum = 0

    def get_stat(self):
        self.collect()
        sort = self.sorting()
        self.print_stat(sort)

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char not in self.stat and char.isalpha():
                        self.stat[char] = 1
                    elif char in self.stat:
                        self.stat[char] += 1

    def sorting(self):
        pass

    def print_stat(self, sort):
        print('+---------+----------+')
        print('|{txt:^9}|'.format(txt='char'), '{txt:^9}|'.format(txt='frequency'))
        print('+---------+----------+')

        for i in range(len(sort)):
            print('|{txt:^9}|'.format(txt=sort[i][0]),
                  '{txt:^9}|'.format(txt=sort[i][1]))
            self.sum += sort[i][1]

        print('+---------+----------+')
        print('|{txt:^9}|'.format(txt='total'), '{txt:^9}|'.format(txt=self.sum))
        print('+---------+----------+')


class AlphabeticUpward(Statistics):
    def sorting(self):
        return sorted(self.stat.items(), key=lambda num: num[0])


class AlphabeticDownward(Statistics):
    def sorting(self):
        return sorted(self.stat.items(), key=lambda num: num[0], reverse=True)


class ValueUpward(Statistics):
    def sorting(self):
        return sorted(self.stat.items(), key=lambda num: num[1])


class ValueDownward(Statistics):
    def sorting(self):
        return sorted(self.stat.items(), key=lambda num: num[1], reverse=True)


alphabetic_up = AlphabeticUpward(file_name='files/voyna-i-mir.txt.zip')
alphabetic_down = AlphabeticDownward(file_name='files/voyna-i-mir.txt.zip')
value_up = ValueUpward(file_name='files/voyna-i-mir.txt.zip')
value_down = ValueDownward(file_name='files/voyna-i-mir.txt.zip')

alphabetic_up.get_stat()
# alphabetic_down.get_stat()
# value_up.get_stat()
# value_down.get_stat()
