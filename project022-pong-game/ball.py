from turtle import Turtle
import time

BALL_WIDTH = 0.5

class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.move_speed = 0.1
        self.move_distance = 12
        self.x_direction = self.move_distance
        self.y_direction = self.move_distance
        self.create_ball()

    def create_ball(self):
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=BALL_WIDTH)
        self.penup()

    def move(self):
        """A function to move the ball"""
        next_x = self.xcor() + self.x_direction
        next_y = self.ycor() + self.y_direction
        self.goto(next_x, next_y)

    def bounce(self, direction):
        """A function to reverse the ball direction"""
        if direction == 'vertical':
            self.y_direction *= -1
        elif direction == 'horizontal':
            self.x_direction *= -1
            self.move_speed *= 0.9


    def reset_position(self):
        self.home()
        self.bounce('horizontal')
        self.screen.update()
        self.move_speed = 0.1
        time.sleep(0.75)
