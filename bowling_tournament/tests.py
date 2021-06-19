import unittest
from score_count_engine import Bowling, FirstThrowState


class BowlingScoreTestOld(unittest.TestCase):

    def setUp(self):
        self.bowling = Bowling(game_result='3532X332/3/62--62X', state=FirstThrowState(), count_rules='old')

    def test_score(self):
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 105)

    def test_frames(self):
        self.bowling.frame = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.frame, 10)

    def test_all_strikes(self):
        self.bowling = Bowling(game_result='XXXXXXXXXX', state=FirstThrowState(), count_rules='old')
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 200)

    def test_all_misses(self):
        self.bowling = Bowling(game_result='--------------------', state=FirstThrowState(), count_rules='old')
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 0)

    def test_all_spares(self):
        self.bowling = Bowling(game_result='-/-/-/-/-/-/-/-/-/-/', state=FirstThrowState(), count_rules='old')
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 150)

    def test_all_numbers(self):
        self.bowling = Bowling(game_result='12344521431234452143', state=FirstThrowState(), count_rules='old')
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 58)

    def test_wrong_number_of_frames(self):
        self.bowling = Bowling(game_result='123445', state=FirstThrowState(), count_rules='old')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Wrong number of frames' in str(context.exception))

    def test_strike_in_second_throw(self):
        self.bowling = Bowling(game_result='-X-X-X-X-X', state=FirstThrowState(), count_rules='old')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Strike in second throw' in str(context.exception))

    def test_spare_in_first_throw(self):
        self.bowling = Bowling(game_result='/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-', state=FirstThrowState(),
                               count_rules='old')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Spare in first throw' in str(context.exception))

    def test_wrong_sum_of_points(self):
        self.bowling = Bowling(game_result='558255', state=FirstThrowState(), count_rules='old')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Invalid value entered - the sum of one frame is more than 9 points' in str(context.exception))

    def test_wrong_value(self):
        self.bowling = Bowling(game_result=r'0!\-----------------', state=FirstThrowState(), count_rules='old')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Invalid value entered' in str(context.exception))


class BowlingScoreTestNew(unittest.TestCase):

    def setUp(self):
        self.bowling = Bowling(game_result='3532X332/3/62--62X', state=FirstThrowState(), count_rules='new')

    def test_score(self):
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 90)

    def test_frames(self):
        self.bowling.frame = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.frame, 10)

    def test_all_strikes(self):
        self.bowling = Bowling(game_result='XXXXXXXXXX', state=FirstThrowState(), count_rules='new')
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 270)

    def test_all_misses(self):
        self.bowling = Bowling(game_result='--------------------', state=FirstThrowState(), count_rules='new')
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 0)

    def test_all_spares(self):
        self.bowling = Bowling(game_result='-/-/-/-/-/-/-/-/-/-/', state=FirstThrowState(), count_rules='new')
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 100)

    def test_all_numbers(self):
        self.bowling = Bowling(game_result='12344521431234452143', state=FirstThrowState(), count_rules='new')
        self.bowling.total_points = 0
        self.bowling.analize_result()
        self.assertEqual(self.bowling.total_points, 58)

    def test_wrong_number_of_frames(self):
        self.bowling = Bowling(game_result='123445', state=FirstThrowState(), count_rules='new')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Wrong number of frames' in str(context.exception))

    def test_strike_in_second_throw(self):
        self.bowling = Bowling(game_result='-X-X-X-X-X', state=FirstThrowState(), count_rules='new')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Strike in second throw' in str(context.exception))

    def test_spare_in_first_throw(self):
        self.bowling = Bowling(game_result='/-', state=FirstThrowState(),
                               count_rules='new')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Spare in first throw' in str(context.exception))

    def test_wrong_sum_of_points(self):
        self.bowling = Bowling(game_result='558255', state=FirstThrowState(), count_rules='new')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Invalid value entered - the sum of one frame is more than 9 points' in str(context.exception))

    def test_wrong_value(self):
        self.bowling = Bowling(game_result=r'0!\-----------------', state=FirstThrowState(), count_rules='new')
        with self.assertRaises(ValueError) as context:
            self.bowling.analize_result()
        self.assertTrue('Invalid value entered' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
