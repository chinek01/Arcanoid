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
from board.sBoard import sBoard
from block.block import Block, sBlock
from ball.ball import Ball

from time import sleep
from random import randint


# Game options
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "#323232"

ROWS = 4
COLS = 7

PLAY_SCREEN_WIDTH = 800
PLAY_SCREEN_HEIGHT = SCREEN_HEIGHT - 100

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


block_index = -1


def block_del():

    if len(blocks) > 0:
        blocks[block_index].reset()
        blocks[block_index].hideturtle()
        del(blocks[block_index])


def sBlock_del():
    if len(blocks) > 0:
        for b in blocks[block_index].get_body():
            b.reset()
            b.hideturtle()
        del(blocks[block_index])


def start_game():
    game_core.set_move_ball_flag(True)


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
scoreboard.set_life_info(
    game_core.cur_life
)
scoreboard.refresh()

# init board
# old board
# board = Board(
#     screen_width=SCREEN_WIDTH,
#     screen_height=SCREEN_HEIGHT
# )

# new board
board = sBoard(
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT
)

# init blocks
blocks = []

for row in range(ROWS):
    for col in range(COLS):
        # old blocks
        # blocks.append(Block(
        #     pos_x=-300 + 100 * col,
        #     pos_y=110 - 30 * row,
        #     block_color=BLOCK_COLORS[row]
        # ))
        # new blocks
        blocks.append(
            sBlock(
                color=BLOCK_COLORS[row],
                start_position=[-300 + 100 * col,
                                110 - 30 * row]
            )
        )

# init ball
ball = Ball(
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT,
    screen_top=100,
    screen_bottom=0
)
# ball.goto(0, -(SCREEN_HEIGHT / 2) + 30)
ball.goto(0, -200)
# ball.set_starting_position([0, -200])
ball.set_starting_position([0,
                            -(SCREEN_HEIGHT / 2) + 75])
ball.reset_ball()

# game loop
screen.listen()

screen.onkey(key='a', fun=board.move_left)
screen.onkey(key='Left', fun=board.move_left)

screen.onkey(key='d', fun=board.move_right)
screen.onkey(key='Right', fun=board.move_right)

screen.onkey(key='space', fun=start_game)

# screen.onkey(key='l', fun=block_del)

while game_core.get_game_over_flag():

    screen.update()

    if game_core.move_ball_flag is True:
        ball.move()

    if len(blocks) > 0:
        # hit block detection

        i = 0
        # new blocks
        for my_block in blocks:
            for my_block_blocks in my_block.get_body():
                if ball.distance(my_block_blocks) < 20:
                    ball.y_bounce()
                    block_index = i
                    sBlock_del()
                    scoreboard.set_curr_score()
                    break
            i += 1

        # old blocks
        # for my_block in blocks:
        #     if ball.distance(my_block) < 20:
        #         block_index = i
        #         block_del()
        #         ball.y_bounce()
        #         break
        #     i += 1

    # ball out of game board
    if ball.ycor() < -(SCREEN_HEIGHT / 2) + 10:
        print("loose life")
        game_core.loose_life()
        game_core.set_move_ball_flag(False)
        scoreboard.set_life_info(
            game_core.cur_life
        )
        scoreboard.refresh()
        ball.reset_ball()
        board.reset_board()

    # ball detection collision with board
    # old board collision detection
    # if ball.distance(board) < 20:
    #     ball.y_bounce()

    # new board collision detection
    for board_segment in board.get_body():
        if ball.distance(board_segment) < 20:
            ball.y_bounce()

    sleep(0.05)

# exit
screen.exitonclick()
