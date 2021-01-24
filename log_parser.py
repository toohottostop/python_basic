from datetime import datetime
from collections import Counter
import tabulate


class LogParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.data_list = []
        self.group_by = {}

    def parse(self, out_file_name):
        self.collect_data()
        self.out_file(out_file_name)

    def collect_data(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    data = datetime.fromisoformat(line[1:17])
                    self.data_list.append(data)

    def out_file(self, out_file_name=None):
        if out_file_name is not None:
            out_file = open(out_file_name, 'w', encoding='utf8')
            self.event_by_minute(out_file)
            self.event_by_hour(out_file)
            self.event_by_month(out_file)
            self.event_by_year(out_file)
        else:
            out_file = None
        out_file.close()

    def event_by_minute(self, out_file):
        pass

    def event_by_hour(self, out_file):
        pass

    def event_by_month(self, out_file):
        pass

    def event_by_year(self, out_file):
        pass


class ParsingByMinute(LogParser):

    def event_by_minute(self, out_file):
        counted_by_minute = Counter(self.data_list)
        for date, count in counted_by_minute.items():
            out_file.write('[{}] : {}\n'.format(date.strftime('%Y-%m-%d %H:%M'), str(count)))


class ParsingByHour(LogParser):

    def event_by_hour(self, out_file):
        for date in self.data_list:
            if date.strftime('%H') not in self.group_by:
                self.group_by.setdefault(date.strftime('%H'), date.strftime('%Y-%m-%d %H:%M' + '\n'))
            else:
                self.group_by[date.strftime('%H')] += date.strftime('%Y-%m-%d %H:%M' + '\n')
        out_file.write(tabulate.tabulate(self.group_by.items(), headers=['Hour', 'Date'], tablefmt='grid',
                                         stralign='center'))


class ParsingByMonth(LogParser):

    def event_by_month(self, out_file):
        for date in self.data_list:
            if date.strftime('%m') not in self.group_by:
                self.group_by.setdefault(date.strftime('%m'), date.strftime('%Y-%m-%d %H:%M' + '\n'))
            else:
                self.group_by[date.strftime('%m')] += date.strftime('%Y-%m-%d %H:%M' + '\n')
        out_file.write(tabulate.tabulate(self.group_by.items(), headers=['Month', 'Date'], tablefmt='grid',
                                         stralign='center'))


class ParsingByYear(LogParser):

    def event_by_year(self, out_file):
        for date in self.data_list:
            if date.strftime('%Y') not in self.group_by:
                self.group_by.setdefault(date.strftime('%Y'), date.strftime('%Y-%m-%d %H:%M' + '\n'))
            else:
                self.group_by[date.strftime('%Y')] += date.strftime('%Y-%m-%d %H:%M' + '\n')
        out_file.write(tabulate.tabulate(self.group_by.items(), headers=['Year', 'Date'], tablefmt='grid',
                                         stralign='center'))


by_minute = ParsingByMinute(file_name='files/events.txt')
by_hour = ParsingByHour(file_name='files/events.txt')
by_month = ParsingByMonth(file_name='files/events.txt')
by_year = ParsingByYear(file_name='files/events.txt')

by_minute.parse(out_file_name='files/out.txt')
# by_hour.parse(out_file_name='files/out.txt')
# by_month.parse(out_file_name='files/out.txt')
# by_year.parse(out_file_name='files/out.txt')
