import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=550)
screen.bgcolor('white')
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=player.move)
screen.onkey(key='w', fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    for car in car_manager.all_car:
        if player.distance(car) < 20:
            Scoreboard.game_over()
            game_is_on = False

    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        score_board.increase_level()
        car_manager.increase_speed()

screen.exitonclick()
