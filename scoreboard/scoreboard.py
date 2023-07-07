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
import csv

FONT = ("Arial", 25, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self,
                 screen_width=800,
                 screen_height=600,
                 score_file_path=None):
        super().__init__()
        self.shape('square')
        self.color('gray')
        self.penup()
        self.hideturtle()
        self.screen_width = screen_width
        self.screen_height = screen_height

        if score_file_path is None:
            raise ValueError("The Score file path must be set!")

        self._score_file_path = score_file_path
        self._score_data = None

    def read_results_from_file(self):
        """
        Read score file
        """
        with open(self._score_file_path, 'r') as f:
            self._score_data = list(csv.reader(f))


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

    x = Scoreboard(score_file_path='../score_data.csv')
    x.read_results_from_file()

    screen.update()
    screen.exitonclick()
