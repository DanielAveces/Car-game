from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.l_score}", align="center", font=(FONT))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=(FONT))
