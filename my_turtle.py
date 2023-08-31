from turtle import Turtle

# Constants
MOVEMENT = 20


class My_Turtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.x_pos = -230
        self.reset_position()

    def move_up(self):
        self.x_pos = self.x_pos + MOVEMENT
        self.goto(0, self.x_pos)

    def move_down(self):
        self.x_pos = self.x_pos - MOVEMENT
        if self.x_pos < -240:
            self.reset_position()
        self.goto(0, self.x_pos)

    def reset_position(self):
        self.x_pos = -230
        self.goto(0, self.x_pos)
