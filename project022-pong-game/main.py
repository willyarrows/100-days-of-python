import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_right = Paddle(init_pos=(SCREEN_WIDTH/2 - 50, 0), screen=screen)
paddle_left = Paddle(init_pos=(-1 * SCREEN_WIDTH/2 + 40, 0), screen=screen)
ball = Ball(screen=screen)

screen.listen()
screen.onkey(key="Up", fun=paddle_right.up)
screen.onkey(key="Down", fun=paddle_right.down)
screen.onkey(key="w", fun=paddle_left.up)
screen.onkey(key="s", fun=paddle_left.down)

game_is_on = True

y_ceiling = SCREEN_HEIGHT / 2 - 10
y_floor = -1 * SCREEN_HEIGHT / 2 + 30

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() >= y_ceiling or ball.ycor() <= y_floor:
        ball.bounce('vertical')

    if (((ball.xcor() >= SCREEN_WIDTH/2 - 70) and ball.distance(paddle_right) <= 40)
            or ((ball.xcor() <= -1 * SCREEN_WIDTH / 2 + 60) and ball.distance(paddle_left) <= 40)):
        ball.bounce('horizontal')

    if ball.xcor() > SCREEN_WIDTH / 2:
        ball.reset_position()

    if ball.xcor() < -1 * SCREEN_WIDTH / 2:
        ball.reset_position()

screen.exitonclick()
