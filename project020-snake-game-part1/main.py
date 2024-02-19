import time
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Glorious Snake Game')
screen.tracer(0)

snake = Snake()
screen.update()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
