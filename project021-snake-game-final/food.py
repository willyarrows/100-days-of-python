from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Randomly refresh food position in a new location"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-255, 255)
        self.goto(random_x, random_y)
