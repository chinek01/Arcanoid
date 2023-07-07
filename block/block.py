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
        self.shape('square')
        self.color('white')
        self._block_size = 4
        self.shapesize(
            stretch_len=self._block_size,
            stretch_wid=1
        )

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

    x = Block()

    screen.update()
    screen.exitonclick()
