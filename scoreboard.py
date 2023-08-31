from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-230, 230)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level : {self.level}", align="left", font=("Courier", 12, "normal"))

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 220)
        self.write(arg=f"GAME OVER", align="center", font=("Courier", 12, "normal"))

    def won(self):
        self.goto(0, 220)
        self.write(arg=f"YOU WON!", align="center", font=("Courier", 12, "normal"))
