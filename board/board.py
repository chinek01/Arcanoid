"""

Portfolio: Arcanoid Game

Board class

#100DaysOfCode with Python
Day: 86
Date: 2023-07-06
Author: MC

"""

from turtle import Turtle
from turtle import Screen


class Board(Turtle):

    def __init__(self,
                 screen_width=800,
                 screen_height=600):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self._board_size = 8
        self.shapesize(
            stretch_len=self._board_size,
            stretch_wid=1
        )
        self.screen_width = screen_width
        self.screen_height = screen_height
        self._starting_position = [0,
                                   -self.screen_height/2 + 30]
        self.goto(self._starting_position[0],
                  self._starting_position[1])

    def move_left(self):
        pass

    def move_right(self):
        pass

    def _move(self,
              new_x):
        pass

    def set_starting_position(self,
                              position):
        """
        set starting position for thr Board
        :param position: [x, y] - co-ordinates
        """

        if not isinstance(position, list):
            raise TypeError("Variable position must be list")

        self._starting_position = position

    def get_starting_position(self):
        return self._starting_position

    def reset_board(self):
        self.goto(self.get_starting_position()[0],
                  self.get_starting_position()[1])

    def set_board_size(self,
                       size=5):
        """
        set board size
        :param size: default 5 - int type
        :return:
        """
        if not isinstance(size, int):
            raise TypeError("Size must be int type!")

        self._board_size = size

    def get_board_size(self):
        """
        :return: current board size
        """
        return self._board_size


# some test
if __name__ == '__main__':
    # screen init
    width = 800
    height = 600
    screen = Screen()
    screen.title("Board test")
    screen.setup(
        width=width,
        height=height
    )
    screen.bgcolor("#323232")
    screen.tracer(0)

    x = Board(width,
              height)
    # x.set_starting_position([0, -250])
    # x.reset_board()

    screen.update()
    screen.exitonclick()
