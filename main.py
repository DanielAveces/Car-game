from scoreboard import Scoreboard
from turtle import Turtle, Screen
from cars import Car
import time
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
time_spent = 0.1

game_is_on = True

my_list = []
car = Car()

for i in range(0, 150):
    i = Car()
    my_list.append(i)

tim = Player()
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(time_spent)
    screen.update()

    screen.onkey(tim.up, "Up")
    screen.onkey(tim.down, "Down")

    for r in my_list:
        r.movement()
        if r.distance(tim) < 28:
            tim.goal()
            scoreboard.game_over()
            game_is_on = False

    if tim.ycor() >= 280:
        tim.goal()
        car.increment()
        scoreboard.l_point()



screen.exitonclick()