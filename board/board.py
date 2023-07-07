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

from time import sleep


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
        self._y_pos = -self.screen_height/2 + 30    # const board y pos
        self._max_left_pos = 0
        self._max_right_pos = 0
        self._max_left_right()
        self._starting_position = [0,
                                   self._y_pos]
        self.goto(self._starting_position[0],
                  self._starting_position[1])
        self._move_distance = 20

    def _max_left_right(self):
        """
        Calculater max left/right max move possibilities.
        :return:
        """
        space_board = (self._board_size * 20) / 2
        self._max_left_pos = -self.screen_width/2 + space_board
        self._max_right_pos = self.screen_width/2 - space_board

    def move_left(self):
        new_x = self.xcor() - self._move_distance
        if new_x >= self._max_left_pos:
            self._move(new_x)

    def move_right(self):
        new_x = self.xcor() + self._move_distance
        if new_x <= self._max_right_pos:
            self._move(new_x)

    def _move(self,
              new_x):
        self.goto(
            new_x,
            self._y_pos
        )

    def set_move_distance(self,
                          move_distance):
        """
        Set move distance parameter
        :param move_distance: distance as type int
        :return:
        """
        if not isinstance(move_distance, int):
            raise TypeError("Variable distance must by int type.")

        self._move_distance = move_distance

    def get_move_distance(self):
        return self._move_distance

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
        self._max_left_right()

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

    screen.listen()
    screen.onkey(key="Left", fun=x.move_left)
    screen.onkey(key='a', fun=x.move_left)
    screen.onkey(key='Right', fun=x.move_right)
    screen.onkey(key='d', fun=x.move_right)

    while True:
        screen.update()
        sleep(0.001)

    screen.update()
    screen.exitonclick()
