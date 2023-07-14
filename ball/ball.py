"""

Portfolio: Arcanoid Game
#100DaysOfCode with Python
Ball class

Day: 86
Date: 2023-07-06
Author: MC

"""


from turtle import Turtle
from turtle import Screen

from time import sleep

BALL_COLORS = ["#69345F",
               "#171D69",
               "#B57952",
               "#B8B071",
               "#35AEB8",
               "#B8709B",
               "#7E7FB8",
               "#268EB8",
               "#519E21",
               "#6A839E",
               "white"]


class Ball(Turtle):

    def __init__(self,
                 screen_width=800,
                 screen_height=600,
                 screen_top=100,
                 screen_bottom=0):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=0.5,
                       stretch_len=0.5)
        self.penup()
        self._move_speed = 0.1
        self._starting_position = [0, 0]
        self._move_distance = 10
        self.x_move = self._move_distance
        self.y_move = self._move_distance

        # playground dimensions
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.top_margin = screen_top
        self.bottom_margin = screen_bottom
        self._max_left_pos = 0
        self._max_right_pos = 0
        self._max_bottom_pos = 0
        self._max_top_pos = 0
        self.max_left_right()

    def max_left_right(self):
        """
        Calculate max left and right pos
        """
        # ball dimensions 10x10 px
        self._max_left_pos = -self.screen_width/2 + 10
        self._max_right_pos = self.screen_width/2 - 10
        self._max_bottom_pos = -self.screen_height/2 + self.bottom_margin + 10
        self._max_top_pos = self.screen_height/2 - self.top_margin - 30

    def set_move_distance(self,
                          distance=10):
        """
        Set distance value.
        :param distance: as int
        """

        if not isinstance(distance, int):
            raise ValueError("The Distance must be int value!")

        self._move_distance = distance

    def get_move_distance(self):
        """
        :return: distance value
        """
        return self._move_distance

    def set_starting_position(self,
                              position):
        """
        set starting position for the Ball
        :param position: [x, y]
        :return:
        """
        self._starting_position = position

    def get_starting_position(self):
        """
        :return: starting position for the Ball as [x, y] values
        """
        return self._starting_position

    def set_move_speed(self,
                       move_speed=0.1):
        """
        Set ball move speed parameter
        :param move_speed: ball speed as float
        """

        if not isinstance(move_speed, float):
            raise ValueError("The Move Speed parameter must be a float value!")

        self._move_speed = move_speed

    def get_move_speed(self) -> float:
        """
        :return: ball move speed
        """
        return self._move_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # print(self._max_left_pos)
        # print(self._max_top_pos)
        # print(self._max_right_pos)
        # print(self._max_bottom_pos)

        if new_x > self._max_right_pos or new_x < self._max_left_pos:
            # print("trafiony x")
            self.x_bounce()

        if new_y > self._max_top_pos or new_y < self._max_bottom_pos:
            # print("trafiony Y")
            self.y_bounce()

        # print(new_x, ' ', new_y)

        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(self.get_starting_position()[0],
                  self.get_starting_position()[1])
        self.x_bounce()


# some test
if __name__ == '__main__':
    # screen init
    width = 800
    height = 600

    screen = Screen()
    screen.title('Ball test')
    screen.setup(
        width=width,
        height=height
    )
    screen.bgcolor('#323232')
    screen.tracer(0)

    x = Ball(screen_width=width,
             screen_height=height,
             screen_top=100,
             screen_bottom=50
             )

    x.set_starting_position([0, 0])
    x.goto(x.get_starting_position()[0],
           x.get_starting_position()[1])
    x.reset_ball()

    while True:
        screen.update()
        sleep(0.05)
        x.move()

    # screen.update()
    screen.exitonclick()
