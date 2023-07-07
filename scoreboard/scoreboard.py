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
        self._read_results_from_file()

        self._max_score = []
        self._find_max_score()

    def _read_results_from_file(self):
        """
        Read score file
        """
        with open(self._score_file_path, 'r') as f:
            self._score_data = list(csv.reader(f))

    def _find_max_score(self):
        """
        Find The Max result
        """
        self._max_score = ['', '0']

        for row in self._score_data:
            # print(row)
            try:
                if int(self._max_score[1]) < int(row[1]):
                    self._max_score = row
            except Exception as e:
                print(f"Some error: {e.__str__()}")


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

    screen.update()
    screen.exitonclick()
