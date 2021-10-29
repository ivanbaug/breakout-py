from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick_manager import BrickManager
import time

# Screen  size
S_WIDTH = 800
S_HEIGHT = 600


# Default turtle size is 20 px by 20 px


screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.bgcolor("black")
screen.title("Ivan's Breakout Game")
screen.listen()
screen.tracer(0)  # update screen on command

# Paddle math for pos x:
# pos x = half the height in negative coordinates +
# half the height of the paddle assuming a total of 20px (default turtle size) +
# float 20 pixels so you can see the ball fall

paddle_pos_x = (-S_HEIGHT / 2) + 10 + 20
pd = Paddle((0, paddle_pos_x), (S_WIDTH, S_HEIGHT))

ball = Ball()

scoreb = Scoreboard()

bm = BrickManager((S_WIDTH, S_HEIGHT))
bm.create_bricks()

# screen.onkeypress(key="Up", fun=rp.move_up)
# screen.onkeypress(key="Down", fun=rp.move_down)

screen.onkeypress(key="Left", fun=pd.move_left)
screen.onkeypress(key="Right", fun=pd.move_right)

# screen.onkeypress(key="w", fun=lp.move_up)
# screen.onkeypress(key="s", fun=lp.move_down)


game_is_on = True

while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    # detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > (S_WIDTH / 2 - 16 - 10) or ball.xcor() < -(S_WIDTH / 2 - 16):
        ball.bounce_x()
    # detect collision with r paddle

    # if (ball.distance(rp) < 50 and ball.xcor() > 320) or (
    #     ball.distance(lp) < 50 and ball.xcor() < -320
    # ):
    #     ball.bounce_x()

    # right paddle misses
    # if ball.xcor() > 380:
    #     scoreb.point_for_l()
    #     ball.reset_position()
    # if ball.xcor() < -380:
    #     scoreb.point_for_r()
    #     ball.reset_position()


screen.exitonclick()
