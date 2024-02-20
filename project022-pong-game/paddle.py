from turtle import Turtle

# Paddle Size attribute
PADDLE_LENGTH = 4
PADDLE_WIDTH = 0.5

# Paddle Movement attribute
MOVE_DISTANCE = 20

# Direction Constant
RIGHT, UP, LEFT, DOWN = (0, 90, 180, 270)


class Paddle(Turtle):
    def __init__(self, init_pos, screen):
        super().__init__()
        self.init_pos = init_pos
        self.screen = screen

        self.create_paddle()

    def create_paddle(self):
        """A function to create a paddle in a given initial position"""
        self.shape('square')
        self.color('white')
        self.setheading(UP)
        self.shapesize(stretch_len=PADDLE_LENGTH, stretch_wid=PADDLE_WIDTH)
        self.penup()
        self.goto(self.init_pos)

    def up(self):
        """A function to move the paddle upward"""
        screen_height = self.screen.window_height()
        y_limit = screen_height / 2 - 60
        if self.ycor() <= y_limit:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE)

    def down(self):
        """A function to move the paddle upward"""
        screen_height = self.screen.window_height()
        y_limit = -1 * screen_height / 2 + 60
        if self.ycor() >= y_limit:
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE)
