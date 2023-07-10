"""

Portfolio: Arcanoid Game

Scoreboard class

#100DaysOfCode with Python
Day: 86
Date: 2023-07-06
Author: MC

"""
import turtle
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

        # self.hideturtle()
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

        self._frame_color = 'white'
        self._frame_height = 100
        self._frame()

        self._text_color = 'white'
        self._curr_score = 0

    def set_curr_score(self):
        self._curr_score += 1
        self.refresh()

    def set_text_color(self,
                       color='white'):

        if not isinstance(color, str):
            raise TypeError("The Color must be str type.")

        self._text_color = color

    def get_text_color(self):
        return self._text_color

    def refresh(self):
        """
        Refresh scoreboard
        """

        self.clear()

        # write max score
        self.hideturtle()
        self.penup()
        self.color(self._text_color)

        first_x = -self.screen_width/4
        first_y = self.screen_height/2 - self._frame_height/2

        self.goto(first_x - 100, first_y)
        self.write(f"Max name: {self._max_score[0]}",
                   font=FONT)

        self.goto(first_x - 100, first_y - 30)
        self.write(f"Max score: {self._max_score[1]}",
                   font=FONT)

        # current score
        self.goto(first_x * (-1) - 100, first_y)
        self.write(f"Current score: {self._curr_score}",
                   font=FONT)

    def set_frame_color(self,
                        color='white'):
        if not isinstance(color, str):
            raise TypeError("The Color must be str type!")

        self._frame_color = color

    def get_frame_color(self):
        return self._frame_color

    def set_frame_height(self,
                         frame_height=100):
        if not isinstance(frame_height, int):
            raise TypeError("The Frame Height must be int type!")

        self._frame_height = frame_height

    def get_frame_height(self):
        return self._frame_height

    def _frame(self):
        """
        Build scoreboard frame
        :return:
        """
        myPen = turtle.Turtle()
        myPen.penup()
        myPen.setposition(
            -self.screen_width/2 + 10,
            self.screen_height/2 - 10
        )
        myPen.color(self._frame_color)
        myPen.pendown()
        myPen.pensize(5)

        for side in range(2):
            myPen.forward(self.screen_width - 30)
            myPen.right(90)
            myPen.forward(self._frame_height - 10)
            myPen.right(90)

        # central frame
        myPen.penup()
        myPen.setposition(
            0,
            self.screen_height/2 - 10
        )
        myPen.pendown()
        myPen.right(90)
        myPen.forward(self._frame_height - 10)
        myPen.penup()

        myPen.hideturtle()

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

    x = Scoreboard(
        score_file_path='../score_data.csv',
        screen_width=width,
        screen_height=height
    )
    # x.add_curr_result('ABX', '123')
    # x.add_curr_result('DEF', '321')

    screen.onkey(key='a', fun=x.set_curr_score)
    x.set_curr_score()

    while True:
        screen.update()

    screen.exitonclick()
