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
from random import choice


BLOCK_COLORS = ["#69345F",
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


class Block(Turtle):

    def __init__(self,
                 pos_x,
                 pos_y,
                 block_color=None):
        super().__init__()
        self.shape('square')

        if block_color is None:
            self.color(choice(BLOCK_COLORS))
        else:
            self.color(block_color)

        self.penup()
        self._block_size = 4
        self.shapesize(
            stretch_len=self._block_size,
            stretch_wid=1
        )
        self._pos_x = pos_x
        self._pos_y = pos_y
        self.goto(self._pos_x,
                  self._pos_y)


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

    x1 = Block(-300, 0)
    x2 = Block(-200, 0)
    x3 = Block(-100, 0)
    x4 = Block(0, 0)
    x5 = Block(100, 0)
    x6 = Block(200, 0)
    x7 = Block(300, 0)

    screen.update()
    screen.exitonclick()
