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
                 move_distance=80):
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._board_size = board_size
        self._color = color

        self._y_pos = -self._screen_height/2 + 30
        self._x_pos_start = 0
        self._max_left_pos = 0
        self._max_right_pos = 0

        self._max_left_right()
        self._move_distance = move_distance

        self._body = []
        self.board()

    def get_body(self):
        return self._body

    def board(self):
        # create board body from left to right
        for n in range(self._board_size):
            self._add_segment(
                color=self._color,
                position=[self._x_pos_start + 20 * n, self._y_pos]
            )

    def _add_segment(self,
                     color,
                     position):
        bb = Turtle('square')
        bb.penup()
        bb.color(color)
        bb.goto(position)
        self._body.append(bb)

    def get_board_size(self):
        return self._board_size

    def set_board_size(self,
                       size=8):
        if not isinstance(size, int):
            raise TypeError("The size value must be int type!")

        self._board_size = size

    def reset_board(self):
        # todo: reset board position
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

    def move_right(self):
        # todo: board move right

        stop_move_flag = False
        for n in range(len(self._body), 0, -1):
            new_x_cor = self._body[n-1].xcor() + self._move_distance
            if new_x_cor <= self._max_right_pos and stop_move_flag is False:
                self._body[n-1].goto(
                    new_x_cor,
                    self._y_pos
                )
            else:
                stop_move_flag = True

    def move_left(self):
        # todo: board move left
        stop_move_flag = False
        for n in range(len(self._body)):
            new_x_cor = self._body[n].xcor() - self._move_distance
            if new_x_cor >= self._max_left_pos and stop_move_flag is False:
                self._body[n].goto(
                    new_x_cor,
                    self._y_pos
                )
            else:
                stop_move_flag = True

    def _max_left_right(self):
        # opcjonalnie dzielenie przez 2 do sprawdzenia
        # todo: check correct max distance left right after move func write
        space_board = (self._board_size * 20) / 2
        # self._max_left_pos = - self._screen_width/2 + space_board
        # self._max_right_pos = self._screen_width/2 - space_board

        self._max_left_pos = - self._screen_width / 2
        self._max_right_pos = self._screen_width / 2

        self._x_pos_start = -self._board_size/2 * 20


# some test
if __name__ == '__main__':
    # screen init
    width = 800
    height = 600
    screen = Screen()
    screen.title("sBoard test")
    screen.setup(
        width=width,
        height=height
    )
    screen.bgcolor("#323232")
    screen.tracer(0)

    # body class
    x = sBoard()
    x.set_move_distance(80)

    screen.listen()
    screen.onkey(key='Left', fun=x.move_left)
    screen.onkey(key='a', fun=x.move_left)
    screen.onkey(key='Right', fun=x.move_right)
    screen.onkey(key='d', fun=x.move_right)

    while True:
        screen.update()
        sleep(0.001)

    screen.exitonclick()
