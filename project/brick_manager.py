from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "blue"]
# COLORS = ["blue"]
BRICK_WIDTH = 3
BRICK_HEIGHT = 1
BRICK_WIDTH_PX = BRICK_WIDTH * 20
BRICK_HEIGHT_PX = BRICK_HEIGHT * 20
MISSING_PX_R = 10
SPACING = 2


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=BRICK_HEIGHT, stretch_len=BRICK_WIDTH)
        self.penup()
        self.color("black")
        self.w = BRICK_WIDTH * 20  # px
        self.h = BRICK_HEIGHT * 20  # px


class BrickManager:
    def __init__(self, window_size):
        self.all_bricks = []
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.max_bricks_x = int(
            (self.window_width - MISSING_PX_R) / (BRICK_WIDTH_PX + SPACING)
        )

    def create_bricks(self):
        space_left_x = (
            self.window_width
            - MISSING_PX_R
            - self.max_bricks_x * (BRICK_WIDTH_PX + SPACING)
        )
        x_start = -self.window_width / 2 + (BRICK_WIDTH_PX / 2) + (space_left_x / 2)
        # x_start = 30
        spacing_top = self.window_height / 2 - BRICK_HEIGHT_PX * 8
        for i, clr in enumerate(COLORS):
            # for j in range(1):
            for j in range(self.max_bricks_x):
                new_brick = Brick()
                new_brick.color(clr)
                new_brick.goto(
                    x_start + (BRICK_WIDTH_PX + SPACING) * j,
                    spacing_top - ((BRICK_HEIGHT_PX + SPACING) * i),
                )
                self.all_bricks.append(new_brick)

    def remove_brick(self, index):
        self.all_bricks[index].hideturtle()
        self.all_bricks[index].clear()
        del self.all_bricks[index]

    # def move_cars(self):
    #     for car in self.all_cars:
    #         car.backward(self.car_speed)

    # def level_up(self):
    #     self.car_speed += MOVE_INCREMENT
