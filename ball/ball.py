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

    def __init__(self):
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
        :return: distance vaule
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
    screen = Screen()
    screen.title('Ball test')
    screen.setup(
        width=800,
        height=600
    )
    screen.bgcolor('#323232')
    screen.tracer(0)

    x = Ball()

    x.set_starting_position([0, 200])
    x.goto(x.get_starting_position()[0],
           x.get_starting_position()[1])

    screen.update()
    screen.exitonclick()
