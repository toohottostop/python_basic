from datetime import datetime
from collections import Counter
import tabulate


class LogParser:

    def __init__(self, file_name, out_file_name):
        self.file_name = file_name
        self.out_file_name = out_file_name
        self.date_parse_by = None
        self.group_by = {}

    def parse(self):
        self.collect_data()
        self.out_file()

    def collect_data(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    date = line[1:self.date_parse_by]
                    count = 0
                    if date not in self.group_by:
                        count += 1
                        self.group_by.setdefault(date, count)
                    else:
                        self.group_by[date] += 1

    def out_file(self):
        with open(self.out_file_name, 'w', encoding='utf8') as out_file:
            for date, value in self.group_by.items():
                out_file.write('[{}]: {}\n'.format(date, str(value)))


class ParsingByMinute(LogParser):

    def __init__(self, file_name, out_file_name):
        super().__init__(file_name, out_file_name)
        self.date_parse_by = 17


class ParsingByHour(LogParser):

    def __init__(self, file_name, out_file_name):
        super().__init__(file_name, out_file_name)
        self.date_parse_by = 14


class ParsingByMonth(LogParser):

    def __init__(self, file_name, out_file_name):
        super().__init__(file_name, out_file_name)
        self.date_parse_by = 8


class ParsingByYear(LogParser):

    def __init__(self, file_name, out_file_name):
        super().__init__(file_name, out_file_name)
        self.date_parse_by = 5


by_minute = ParsingByMinute(file_name='files/events.txt', out_file_name='files/out.txt')
by_hour = ParsingByHour(file_name='files/events.txt', out_file_name='files/out.txt')
by_month = ParsingByMonth(file_name='files/events.txt', out_file_name='files/out.txt')
by_year = ParsingByYear(file_name='files/events.txt', out_file_name='files/out.txt')

by_minute.parse()
# by_hour.parse()
# by_month.parse()
# by_year.parse()
