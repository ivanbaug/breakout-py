from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue"]
BRICK_WIDTH = 2
BRICK_HEIGHT = 1
BRICK_WIDTH_PX = BRICK_WIDTH * 20
BRICK_HEIGHT_PX = BRICK_HEIGHT * 20
MISSING_PX_R = 10
SPACING = 2


class BrickManager:
    def __init__(self, window_size):
        self.all_bricks = []
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.max_bricks_x = int(
            (self.window_width - MISSING_PX_R) / (BRICK_WIDTH_PX + SPACING)
        )

    def create_bricks(self):
        x_start = -self.window_width / 2 + (BRICK_WIDTH_PX / 2 + SPACING)
        for i in range(self.max_bricks_x):

            new_brick = Turtle("square")
            new_brick.shapesize(stretch_wid=BRICK_HEIGHT, stretch_len=BRICK_WIDTH)
            new_brick.penup()
            new_brick.color(COLORS[0])
            print(x_start + (BRICK_WIDTH_PX + SPACING) * i)
            new_brick.goto(x_start + (BRICK_WIDTH_PX + SPACING) * i, 0)
            self.all_bricks.append(new_brick)

    # def move_cars(self):
    #     for car in self.all_cars:
    #         car.backward(self.car_speed)

    # def level_up(self):
    #     self.car_speed += MOVE_INCREMENT
