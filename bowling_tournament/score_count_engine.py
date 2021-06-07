from abc import abstractmethod


class State:

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def points_in_frame_old(self, point):
        pass

    @abstractmethod
    def points_in_frame_new(self, throw, point):
        pass


class FirstThrowState(State):

    def points_in_frame_old(self, point):
        if point == '/':
            raise ValueError('Spare in first throw')
        elif point not in 'X-123456789':
            raise ValueError('Invalid value entered')
        elif point == 'X':
            self.context.total_points += 20
            self.context.frame += 1
        elif point == '-':
            self.context.first_throw_point_cache = point
            self.context.change_state(SecondThrowState())
        else:
            self.context.first_throw_point_cache = point
            self.context.change_state(SecondThrowState())

    def points_in_frame_new(self, throw, point):
        try:
            if '/' in self.context.game_result_dict[throw]:
                raise ValueError('Spare in first throw')
            elif self.context.game_result_dict[throw] not in 'X-123456789':
                raise ValueError('Invalid value entered')
            elif 'X' in self.context.game_result_dict[throw]:
                if 'X' in self.context.game_result_dict[throw + 1]:
                    if 'X' in self.context.game_result_dict[throw + 2]:
                        self.context.total_points += 30
                    elif '/' in self.context.game_result_dict[throw + 2]:
                        self.context.total_points += 30
                    elif '-' in self.context.game_result_dict[throw + 2]:
                        self.context.total_points += 20
                    elif self.context.game_result_dict[throw + 2] == 'X':
                        pass
                    else:
                        self.context.total_points += 20 + int(self.context.game_result_dict[throw + 2])
                    self.context.frame += 1
                elif '/' in self.context.game_result_dict[throw + 1]:
                    raise ValueError('Spare in first throw')
                elif '/' in self.context.game_result_dict[throw + 2]:
                    self.context.total_points += 20
                    self.context.frame += 1
                elif '-' in self.context.game_result_dict[throw + 1]:
                    self.context.total_points += 10
                    self.context.frame += 1
                elif self.context.game_result_dict[throw + 1] == 'X':
                    pass
                else:
                    if '-' in self.context.game_result_dict[throw + 2]:
                        self.context.total_points += 10 + int(self.context.game_result_dict[throw + 1]) + 0
                    else:
                        self.context.total_points += 10 + int(self.context.game_result_dict[throw + 1]) + \
                                                     int(self.context.game_result_dict[throw + 2])
                    self.context.frame += 1
            elif '-' in self.context.game_result_dict[throw]:
                if self.context.game_result_dict[throw + 1] in '123456789':
                    self.context.total_points += int(self.context.game_result_dict[throw + 1])
                self.context.change_state(SecondThrowState())
            elif '/' in self.context.game_result_dict[throw + 1]:
                self.context.change_state(SecondThrowState())
            else:
                self.context.change_state(SecondThrowState())
        except KeyError:
            try:
                if 'X' in self.context.game_result_dict[throw + 1]:
                    self.context.total_points += 20
                    self.context.frame += 1
                elif '/' in self.context.game_result_dict[throw + 2]:
                    self.context.total_points += 20
                    self.context.change_state(SecondThrowState())
            except KeyError:
                self.context.total_points += 10
                self.context.frame += 1


class SecondThrowState(State):

    def points_in_frame_old(self, point):
        if point == 'X':
            raise ValueError('Strike in second throw')
        elif point not in '/-123456789':
            raise ValueError('Invalid value entered')
        elif point == '/':
            self.context.total_points += 15
        elif point == '-' and self.context.first_throw_point_cache == '-':
            self.context.total_points += 0
        elif point == '-' and self.context.first_throw_point_cache.isdigit:
            self.context.total_points += int(self.context.first_throw_point_cache)
        elif point.isdigit and self.context.first_throw_point_cache == '-':
            self.context.total_points += int(point)
        else:
            if int(point) + int(self.context.first_throw_point_cache) >= 10:
                raise ValueError('Invalid value entered - the sum of one frame is more than 9 points')
            self.context.total_points += int(point) + int(self.context.first_throw_point_cache)
        self.context.frame += 1
        self.context.change_state(FirstThrowState())

    def points_in_frame_new(self, throw, point):
        try:
            if 'X' in self.context.game_result_dict[throw]:
                raise ValueError('Strike in second throw')
            elif self.context.game_result_dict[throw] not in '/-123456789':
                raise ValueError('Invalid value entered')
            elif '/' in self.context.game_result_dict[throw]:
                if '/' in self.context.game_result_dict[throw + 1]:
                    raise ValueError('Spare in first throw')
                elif 'X' in self.context.game_result_dict[throw + 1]:
                    self.context.total_points += 20
                elif '-' in self.context.game_result_dict[throw + 1]:
                    self.context.total_points += 10
                else:
                    self.context.total_points += 10 + int(self.context.game_result_dict[throw + 1])
                self.context.change_state(FirstThrowState())
            elif '-' in self.context.game_result_dict[throw]:
                if self.context.game_result_dict[throw - 1] in '123456789':
                    self.context.total_points += int(self.context.game_result_dict[throw - 1])
                self.context.change_state(FirstThrowState())
            else:
                if '-' in self.context.game_result_dict[throw - 1]:
                    self.context.change_state(FirstThrowState())
                elif int(self.context.game_result_dict[throw]) + int(self.context.game_result_dict[throw - 1]) >= 10:
                    raise ValueError('Invalid value entered - the sum of one frame is more than 9 points')
                else:
                    self.context.total_points += int(self.context.game_result_dict[throw]) + \
                                                 int(self.context.game_result_dict[throw - 1])
                self.context.change_state(FirstThrowState())
        except KeyError:
            self.context.total_points += 10
        self.context.frame += 1


class Bowling:

    def __init__(self, game_result, state, count_rules):
        self.count_rules = count_rules
        self.game_result = game_result
        self.game_result_dict = {throw: point for throw, point in enumerate(game_result)}
        self.first_throw_point_cache = 0
        self.frame = 0
        self.total_points = 0
        self._state = state
        self.change_state(state)

    def change_state(self, state):
        self._state = state
        self._state.context = self

    def analize_result(self):
        if self.count_rules == 'old':
            for point in self.game_result:
                self._state.points_in_frame_old(point=point)
        else:
            for throw, point in self.game_result_dict.items():
                self._state.points_in_frame_new(throw=throw, point=point)
        if self.frame != 10:
            raise ValueError('Wrong number of frames')


if __name__ == '__main__':
    bowling = Bowling(game_result='3532X332/3/62--62X', state=FirstThrowState(), count_rules='new')
    bowling.analize_result()
    print(f'{bowling.total_points}')
