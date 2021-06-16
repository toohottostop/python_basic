import argparse

from score_count_engine import Bowling, FirstThrowState

"""Counting according to the old rules"""
# parser = argparse.ArgumentParser(description='Fill the ticket')
# parser.add_argument('-result', type=str, help='enter your result')
# args = parser.parse_args('-result 3532X332/3/62--62X'.split())
#
# game_result = args.result
# bowling = Bowling(game_result=game_result, state=FirstThrowState(), count_rules='old')
# bowling.analize_result()
# print(f'{game_result} - {bowling.total_points}')


"""Counting according to the new rules"""
parser = argparse.ArgumentParser(description='Fill the ticket')
parser.add_argument('-result', type=str, help='enter your result')
parser.add_argument('-count_rules', type=str, help='choose how to count: old rules or new rules')
args = parser.parse_args('-result 3532X332/3/62--63X -count_rules new'.split())

game_result = args.result
count_rules = args.count_rules
bowling = Bowling(game_result=game_result, state=FirstThrowState(), count_rules=count_rules)
bowling.analize_result()
print(f'{game_result} - {bowling.total_points}')
