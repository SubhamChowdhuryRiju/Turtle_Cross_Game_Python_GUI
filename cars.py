from turtle import Turtle
from random import choice, randint

# Constant
colors = ["red", "yellow", "green", "blue"]
MOVEMENT = 10
CAR_SPEEDUP = 0.7


class Car:

    def __init__(self):
        self.cars = []
        self.car_speed = 0.1

    def create_car(self):
        random_create = randint(1, 6)
        if random_create == 1:
            new_car = Turtle(shape="square")
            new_car.color(choice(colors))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_y = randint(-150, 150)
            new_car.goto(250, new_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(MOVEMENT)

    def level_up(self):
        self.car_speed *= CAR_SPEEDUP
