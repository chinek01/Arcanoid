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


class sBlock:

    def __init__(self,
                 start_position,
                 color=None):
        self._body = []
        self._body_size = 4

        if color is None:
            self._block_color = choice(BLOCK_COLORS)
        else:
            self._block_color = color

        if start_position is None:
            raise ValueError("Start position value must be set!")

        self.start_position = start_position
        self.block()

    def block(self):

        # create body from left to right
        for n in range(self._body_size):
            self.add_segment(
                color=self._block_color,
                position=[
                    self.start_position[0] - 20 * n,
                    self.start_position[1]]
            )

    def add_segment(self,
                    color,
                    position):
        bb = Turtle('square')
        bb.penup()
        bb.color(color)
        bb.goto(position)
        self._body.append(bb)

    def set_body_size(self,
                      body_size=4):
        if not isinstance(body_size, int):
            raise TypeError("The Body size value must be int type.")

        self._body_size = body_size

    def get_body_size(self) -> int:
        return self._body_size

    def get_body(self):
        return self._body


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

    # new blocks
    x1 = sBlock([-300, 0])
    x2 = sBlock([-200, 0])
    x3 = sBlock([-100, 0])
    x4 = sBlock([0, 0])
    x5 = sBlock([100, 0])
    x6 = sBlock([200, 0])
    x7 = sBlock([300, 0])

    # old blocks
    # x1 = Block(-300, 0)
    # x2 = Block(-200, 0)
    # x3 = Block(-100, 0)
    # x4 = Block(0, 0)
    # x5 = Block(100, 0)
    # x6 = Block(200, 0)
    # x7 = Block(300, 0)

    screen.update()
    screen.exitonclick()
