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
        self._curr_result = []

    def add_curr_result(self,
                        name,
                        score):
        """
        Add new result to win table
        :param name: games name as ABC
        :param score: points as str
        """

        if name is None:
            raise ValueError("The Name must be set!")
        if not isinstance(name, str):
            raise TypeError("The Name must be str value!")

        if score is None:
            raise ValueError("The Score must be set!")
        if not isinstance(score, str):
            raise TypeError("The Score must be str value!")

        self._curr_result = [name, score]
        self._score_data.append(self._curr_result)

        self._save_results_to_file()
        self._find_max_score()

    def _save_results_to_file(self):
        """
        Save result list to file
        """
        try:
            with open(self._score_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self._score_data)
        except Exception as e:
            print(f"Something bad happened {e.__str__()}")

    def _read_results_from_file(self):
        """
        Read score file
        """
        try:
            with open(self._score_file_path, 'r') as f:
                self._score_data = list(csv.reader(f))
        except Exception as e:
            print(f"Something bad happened {e.__str__()}")

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
    # x.add_curr_result('ABX', '123')
    # x.add_curr_result('DEF', '321')

    screen.update()
    screen.exitonclick()
