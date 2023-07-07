"""

Portfolio: Arcanoid Game

Scoreboard class

#100DaysOfCode with Python
Day: 86
Date: 2023-07-06
Author: MC

"""


from turtle import Turtle
from turtle import Screen

FONT = ("Arial", 25, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self,
                 screen_width=800,
                 screen_height=600):
        super().__init__()
        self.shape('square')
        self.color('gray')
        self.penup()
        self.hideturtle()
        self.screen_width = screen_width
        self.screen_height = screen_height




# some test
if __name__ == '__main__':
    # screen init
    width = 800
    height = 600
    screen = Screen()
    screen.title("Scoreboard test")
    screen.setup(
        width=width,
        height=height
    )
    screen.bgcolor('#323232')
    screen.tracer(0)

    x = Scoreboard()

    screen.update()
    screen.exitonclick()
