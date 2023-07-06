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

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self._board_size = 8
        self.shapesize(
            stretch_len=self._board_size,
            stretch_wid=1
        )

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
    screen = Screen()
    screen.title("Board test")
    screen.setup(
        width=800,
        height=600
    )
    screen.bgcolor("#323232")
    screen.tracer(0)

    x = Board()

    screen.update()
    screen.exitonclick()
