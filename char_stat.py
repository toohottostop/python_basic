from pprint import pprint
import zipfile


class Statistics:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.sum = 0

    def collect(self, how_to_sort):
        # self.unzip()
        self.collect_lines()
        # self.collect_chars()
        self.print_stat(how_to_sort)

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect_lines(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_chars(line=line[:-1])

    def collect_chars(self, line):
        for char in line:
            if char not in self.stat and char.isalpha():
                self.stat[char] = 1
            elif char in self.stat:
                self.stat[char] += 1

    def sort_upward(self):
        pass

    def sort_downward(self):
        pass

    def print_stat(self, how_to_sort):
        if how_to_sort == 'по возрастанию':
            sort = self.sort_upward()
        else:
            sort = self.sort_downward()
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


class AlphabeticSorting(Statistics):
    def sort_upward(self):
        return sorted(self.stat.items(), key=lambda num: num[0])

    def sort_downward(self):
        return sorted(self.stat.items(), key=lambda num: num[0], reverse=True)


class ValueSorting(Statistics):
    def sort_upward(self):
        return sorted(self.stat.items(), key=lambda num: num[1])

    def sort_downward(self):
        return sorted(self.stat.items(), key=lambda num: num[1], reverse=True)


alphabetic = AlphabeticSorting(file_name='files/voyna-i-mir.txt')
value = ValueSorting(file_name='files/voyna-i-mir.txt')
alphabetic.collect(how_to_sort='upwards')
# value.collect(how_to_sort='downwards')
