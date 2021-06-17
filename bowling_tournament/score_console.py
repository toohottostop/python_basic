import argparse

from score_count_engine import Bowling, FirstThrowState
from tournament_handler import TournamentHandler

"""Counting according to the old rules"""
# parser = argparse.ArgumentParser(description='Fill the ticket')
# parser.add_argument('-result', type=str, help='enter your result')
# args = parser.parse_args('-result 3532X332/3/62--62X'.split())
#
# game_result = args.result
# bowling = Bowling(game_result=game_result, state=FirstThrowState(), count_rules='old')
# bowling.analize_result()
# print(f'{game_result} - {bowling.total_points}')


# """Counting according to the new rules"""
# parser = argparse.ArgumentParser(description='Fill the ticket')
# parser.add_argument('-result', type=str, help='enter your result')
# parser.add_argument('-count_rules', type=str, help='choose how to count: old rules or new rules')
# args = parser.parse_args('-result 3532X332/3/62--63X -count_rules new'.split())
#
# game_result = args.result
# count_rules = args.count_rules
# bowling = Bowling(game_result=game_result, state=FirstThrowState(), count_rules=count_rules)
# bowling.analize_result()
# print(f'{game_result} - {bowling.total_points}')


"""Count scores in tournament_scores.txt"""
parser = argparse.ArgumentParser(description='Fill the ticket')
parser.add_argument('-input', type=str, help='enter tournament file name')
parser.add_argument('-output', type=str, help='enter tournament results file name')
parser.add_argument('-count_rules', type=str, help='choose how to count: old rules or new rules')
args = parser.parse_args('-input tournament_scores.txt -output tournament_result.txt -count_rules new'.split())

input_file_name, output_file_name, count_rules = args.input, args.output, args.count_rules
handler = TournamentHandler(input_file_name=input_file_name, output_file_name=output_file_name, count_rules=count_rules)
handler.run()
