from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, "
                                                          "orange, yellow, green, blue, purple) : ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []
init_x, init_y = (-200, -125)
is_race_on = False
winning_color = None

for color in colors:
    timmy = Turtle(shape="turtle")
    timmy.color(color)
    timmy.penup()
    timmy.goto(x=init_x, y=init_y)
    turtle_list.append(timmy)
    init_y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet.lower() == winning_color.lower():
                print(f"You win !!! The {winning_color} turtle is the winner.")
            else:
                print(f"You lose. The {winning_color} turtle is the winner.")

        distance = random.randint(1, 15)
        turtle.forward(distance)

screen.exitonclick()
