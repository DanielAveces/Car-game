from turtle import Turtle
import random

velocity = 6
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.speed(velocity)
        self.color(random.choice(COLORS))
        y_axix = random.randint(-230, 230)
        x_axix = random.randint(-300, 12000)
        self.goto(x_axix, y_axix)

    def movement(self) -> object:
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def increment(self):
        global STARTING_MOVE_DISTANCE
        global MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        print(STARTING_MOVE_DISTANCE)


