from turtle import Turtle

ORIGIN = (0, 210)  # x=0, y = 290
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(ORIGIN)
        self.score_r = 0
        self.score_l = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(ORIGIN)
        self.write(
            f"{self.score_l}     {self.score_r}", True, align=ALIGNMENT, font=FONT
        )

    def point_for_r(self):
        self.score_r += 1
        self.update_score()

    def point_for_l(self):
        self.score_l += 1
        self.update_score()
