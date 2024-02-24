from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.all_car = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2)
            car.penup()
            car.goto(300, random.randint(-230, 230))
            car.setheading(180)
            self.all_car.append(car)

    def move_cars(self):
        for car in self.all_car:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
