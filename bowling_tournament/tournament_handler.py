from collections import OrderedDict
from tabulate import tabulate

from score_count_engine import Bowling, FirstThrowState


class TournamentHandler:
    def __init__(self, input_file_name, output_file_name, count_rules):
        self.count_rules = count_rules
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.tour_results = OrderedDict()
        self.rating = {}

    def run(self):
        with open(self.input_file_name, 'r', encoding='utf8') as in_file:
            for line in in_file:
                if 'Tour' in line:
                    tour = line[:-1]
                    self.tour_results.setdefault(tour, {
                        'name': [],
                        'score': [],
                        'result': [],
                        'winner': '-'
                    })
                    continue
                elif line.startswith('winner') or line.startswith('\n'):
                    continue
                name, score = line[:-1].replace('\t', ',').split(',')
                try:
                    result = self.score_counter(score)
                    self.tour_results[tour]['name'].append(name)
                    self.tour_results[tour]['score'].append(score)
                    self.tour_results[tour]['result'].append(result)
                except ValueError as error:
                    self.tour_results[tour]['name'].append(name)
                    self.tour_results[tour]['score'].append(score)
                    self.tour_results[tour]['result'].append(error.args[0])
            for _tour, tour_data in self.tour_results.items():
                max_result = max([res if type(res) == int else 0 for res in tour_data['result']])
                if max_result != 0:
                    winner = self.tour_results[_tour]['name'][self.tour_results[_tour]['result'].index(max_result)]
                    self.tour_results[_tour]['winner'] = winner
                else:
                    continue
            self.sort_and_write()
            self.print_rating_table()

    def score_counter(self, score):
        bowling = Bowling(game_result=score, state=FirstThrowState(), count_rules=self.count_rules)
        bowling.analize_result()
        return bowling.total_points

    def sort_and_write(self):
        with open(self.output_file_name, 'w', encoding='utf8') as out_file:
            for _tour, tour_data in self.tour_results.items():
                out_file.write(f'{_tour}\n')
                for name, score, result in zip(tour_data['name'], tour_data['score'], tour_data['result']):
                    name_score_result = f"{name} {score} {result}\n"
                    out_file.write(name_score_result)
                out_file.write(f"winner is {tour_data['winner']}\n")
                out_file.write('\n')

    def print_rating_table(self):
        for _tour, tour_data in self.tour_results.items():
            for name in tour_data['name']:
                if name not in self.rating.keys():
                    self.rating.setdefault(name, {'played matches': 1, 'total victories': 0})
                    if name == tour_data['winner']:
                        self.rating[name]['total victories'] += 1
                else:
                    self.rating[name]['played matches'] += 1
                    if name == tour_data['winner']:
                        self.rating[name]['total victories'] += 1
        rating_list = [[key, value['played matches'], value['total victories']] for key, value in self.rating.items()]
        print(tabulate(rating_list, headers=['Игрок', 'played matches', 'total victories'],
                       tablefmt="grid"))
