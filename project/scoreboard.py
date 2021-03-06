from turtle import Turtle

ORIGIN = (0, -60)  # x=0, y = 290
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


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
        self.score_plyr = 0
        self.start_level = False
        self.level = 1
        self.lives = 6
        self.speed_level = [0.05, 0.04, 0.03, 0.02, 0.01]
        self.update_score("Press space to begin")

    def update_score(self, msg=""):
        self.clear()
        self.goto(ORIGIN)
        self.write(
            f"Level:{self.level}     Score:{self.score_plyr}\nLives:{self.lives}\n\n\n\n{msg}",
            True,
            align=ALIGNMENT,
            font=FONT,
        )

    def point_for_plyer(self):
        self.score_plyr += 1
        self.update_score()

    def begin_level(self):
        self.update_score()
        self.start_level = True

    def level_completed(self):
        self.level += 1
        self.update_score("Press space to begin")
        self.start_level = False

    def game_win(self):
        self.update_score("Congrats, you win!")
        self.start_level = False

    def game_over(self):
        self.update_score("Game over")
        self.start_level = False

    def level_speed(self):
        return self.speed_level[self.level - 1]

    def lost_life(self):
        self.lives -= 1
        self.update_score("Press space to begin")
        self.start_level = False
