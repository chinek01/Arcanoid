"""

Portfolio: Arcanoid Game
#100DaysOfCode with Python
Day: 86
Date: 2023-07-06
Author: MC

"""


from turtle import Screen

from scoreboard.scoreboard import Scoreboard
from game_core.game_core import Game_core
from board.board import Board
from block.block import Block
from ball.ball import Ball

from time import sleep


# Game options
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "#323232"

PLAY_SCREEN_WIDTH = 800
PLAY_SCREEN_HEIGHT = SCREEN_HEIGHT - 100


screen = Screen()
screen.title("Arcanoid by MC")
screen.setup(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT
)
screen.bgcolor("#323232")
screen.tracer(0)

# init game core class
game_core = Game_core()

# init scoreboard
scoreboard = Scoreboard(
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT,
    score_file_path='score_data.csv'
)
scoreboard.refresh()

# init board
board = Board(
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT
)

# init ball
ball = Ball(
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT,
    screen_top=100,
    screen_bottom=0
)
ball.goto(0, 0)
ball.reset_ball()

# game loop
screen.listen()

screen.onkey(key='a', fun=board.move_left)
screen.onkey(key='Left', fun=board.move_left)

screen.onkey(key='d', fun=board.move_right)
screen.onkey(key='Right', fun=board.move_right)

while game_core.get_game_over_flag():
    screen.update()

    ball.move()
    sleep(0.001)


# exit
screen.exitonclick()

