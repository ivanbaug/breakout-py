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


def det_collision(obj1, obj2):

    x_max_dist = (obj1.w + obj2.w) / 2
    x_dist = abs(obj1.xcor() - obj2.xcor())
    y_max_dist = (obj1.h + obj2.h) / 2
    y_dist = abs(obj1.ycor() - obj2.ycor())
    ratio_x = x_dist / x_max_dist
    ratio_y = y_dist / y_max_dist

    if x_dist <= x_max_dist and y_dist <= y_max_dist:
        if ratio_x > ratio_y:
            print("bounce y")
            return True, False
        else:
            print("bounce x")
            return True, True
    return False, False


def collides_on_x(obj1, obj2):
    y_max_dist = (obj1.h + obj2.h) / 2
    y_dist = abs(obj1.ycor() - obj2.ycor())
    x_max_dist = (obj1.w + obj2.w) / 2
    x_dist = abs(obj1.xcor() - obj2.xcor())

    ratio_x = x_dist / x_max_dist
    ratio_y = y_dist / y_max_dist

    if ratio_x > ratio_y:
        print("bounce y")
        return False
    return True


paddle_pos_x = (-S_HEIGHT / 2) + 10 + 20
pd = Paddle((0, 0), (S_WIDTH, S_HEIGHT))

ball = Ball()

scoreb = Scoreboard()

bm = BrickManager((S_WIDTH, S_HEIGHT))
bm.create_bricks()

game_is_on = True


screen.onkeypress(key="Up", fun=pd.move_up)
screen.onkeypress(key="Down", fun=pd.move_down)

screen.onkeypress(key="Left", fun=pd.move_left)
screen.onkeypress(key="Right", fun=pd.move_right)

while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    # detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > (S_WIDTH / 2 - 16 - 10) or ball.xcor() < -(S_WIDTH / 2 - 16):
        ball.bounce_x()

    for brick in bm.all_bricks:
        collides = det_collision(brick, pd)
        if collides:
            c_x = collides_on_x(brick, ball)
            if c_x:
                ball.bounce_x()
            else:
                ball.bounce_y()
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
