from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.write(f"score: {self.score}", align="center", font=("calibre", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.increase_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("calibre", 24, "normal"))
