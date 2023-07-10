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
        self.game_over_flag = False

    def loose_life(self):
        self.cur_life -= 1
        self.check_life()

    def check_life(self):
        if self.cur_life == 0:
            self.game_over_flag = True

    def get_game_over_flag(self):
        return self.game_over_flag

    def reset(self):
        self.cur_life = LIFE
        self.game_over_flag = False
