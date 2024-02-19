import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 550)
screen.bgcolor('black')
screen.title('My Glorious Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -290 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        game_is_on = False
        score_board.game_over()

    # Detect collision with snake tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
