"""

Portfolio: Arcanoid Game

Snake Board class

#100DaysOfCode with Python
Day: 86
Date: 2023-07-12
Author: MC

"""

from turtle import Turtle, Screen

from time import sleep


class sBoard:

    def __init__(self,
                 screen_width=800,
                 screen_height=600,
                 board_size=8,
                 color='white',
                 move_distance=20):
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._board_size = board_size
        self._color = color

        self._y_pos = -self._screen_height/2 + 30
        self._max_left_pos = 0
        self._max_right_pos = 0

        self._max_left_right()
        self._move_distance = move_distance

    def board(self):
        pass

    def _add_segment(self,
                     color,
                     position):
        pass

    def get_board_size(self):
        return self._board_size

    def set_board_size(self,
                       size=8):
        if not isinstance(size, int):
            raise TypeError("The size value must be int type!")

        self._board_size = size

    def reset_board(self):
        pass

    def get_starting_position(self):
        pass

    def set_starting_position(self,
                              position):
        pass

    def get_move_distance(self):
        return self._move_distance

    def set_move_distance(self,
                          move_distance):
        if move_distance is None:
            raise ValueError("The Move distance value must be set!")

        if not isinstance(move_distance, int):
            raise TypeError("The Move distance value must be int type!")

        self._move_distance = move_distance

    def _move(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def _max_left_right(self):
        pass


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

    # body class

    screen.listen()
    screen.onkey(key='Left', fun=)
    screen.onkey(key='a', fun=)
    screen.onkey(key='Right', fun=)
    screen.onkey(key='d', fun=)

    while True:
        screen.update()
        sleep(0.001)

    screen.exitonclick()
