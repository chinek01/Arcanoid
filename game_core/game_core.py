"""

Portfolio: Arcanoid Game

Game core class

#100DaysOfCode with Python
Day: 86
Date: 2023-07-06
Author: MC

"""

LIFE = 3


class Game_core:

    def __init__(self):
        self.cur_life = LIFE
        self.game_over_flag = True
        self.move_ball_flag = False

    def set_move_ball_flag(self,
                           flag: bool):
        if flag is None:
            raise ValueError("The flag value must be set!")

        if not isinstance(flag, bool):
            raise TypeError("The flag value must be boot type!")

        self.move_ball_flag = flag

    def get_move_ball_flag(self):
        return self.move_ball_flag

    def loose_life(self):
        self.cur_life -= 1
        self.check_life()

    def check_life(self):
        if self.cur_life == 0:
            self.game_over_flag = False

    def get_game_over_flag(self):
        return self.game_over_flag

    def reset(self):
        self.cur_life = LIFE
        self.game_over_flag = True
        self.move_ball_flag = False
