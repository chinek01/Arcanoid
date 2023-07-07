"""

Portfolio: Arcanoid Game

Block class

#100DaysOfCode with Python
Day: 86
Date: 2023-07-06
Author: MC

"""


from turtle import Turtle
from turtle import Screen


class Block(Turtle):

    def __init__(self):
        super().__init__()


# some test
if __name__ == '__main__':
    # screen init
    width = 800
    height = 600
    screen = Screen()
    screen.title("Block test")
    screen.setup(
        width=width,
        height=height
    )
    screen.bgcolor("#323232")
    screen.tracer(0)

    x = Block(width, height)

    screen.update()
    screen.exitonclick()
