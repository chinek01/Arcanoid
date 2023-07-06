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

    screen.update()
    screen.exitonclick()

