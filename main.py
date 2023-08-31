from turtle import Screen
from my_turtle import My_Turtle
from scoreboard import Scoreboard
from cars import Car
import time

screen = Screen()
screen.title("Turtle Cross")
screen.setup(width=500, height=500)
screen.tracer(0)

player = My_Turtle()
score = Scoreboard()
car = Car()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="Down", fun=player.move_down)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(car.car_speed)
    car.create_car()
    car.move_cars()

    # collision with the upper y-axis to level up
    if player.ycor() > 245:
        score.level_up()
        car.level_up()
        player.reset_position()

    # collision with cars
    for c in car.cars:
        if c.distance(player) < 20:
            is_game_on = False
            score.game_over()

    # Winning logic
    if score.level == 20:
        is_game_on = False
        score.won()

screen.exitonclick()
