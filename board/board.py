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
