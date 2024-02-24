from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
RIGHT, UP, LEFT, DOWN = (0, 90, 180, 270)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """A function to create initial snake as defined in STARTING_POSITIONS"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """A function to add snake body segment to a given position"""
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """A function to extend a snake body from its tail"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        A function to move the snake.
        Snake tail(x) will move to tail(x-1).
        Snake head will move forward.
        """
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """A function to move the snake upward"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """A function to move the snake to left direction"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """A function to move the snake to down direction"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """A function to move the snake to right direction"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
