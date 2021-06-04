import argparse
from score_count_engine import game_score

parser = argparse.ArgumentParser(description='Fill the ticket')
parser.add_argument('-result', type=str, help='enter your result')
parser.set_defaults(func=game_score)
args = parser.parse_args('-result X4/34-4--X--2354X'.split())
game_result = args.result
args.func(game_result)
print(f'{game_result} - {game_score(game_result)}')
