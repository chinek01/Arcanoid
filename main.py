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


# Game options
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "#323232"

PLAY_SCREEN_WIDTH = 800
PLAY_SCREEN_HEIGHT = SCREEN_HEIGHT - 100


screen = Screen()
screen.title("Arcanoid by MC")
screen.setup(
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
screen.tracer(0)

# init game core class
game_core = Game_core()

