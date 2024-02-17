# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# print(rgb_list)

import random
from turtle import Turtle, colormode, Screen

rgb_list = [(236, 225, 83), (202, 5, 72), (198, 164, 10), (235, 51, 129), (206, 76, 11), (108, 179, 218),
            (219, 162, 103), (234, 225, 6), (30, 188, 108), (23, 106, 173), (13, 23, 64), (17, 28, 175),
            (213, 135, 176), (9, 185, 214), (205, 29, 142), (229, 168, 197), (125, 189, 162), (8, 49, 28),
            (37, 132, 73), (125, 219, 233), (67, 22, 8), (61, 11, 26), (111, 89, 211), (142, 216, 201), (190, 15, 5),
            (238, 63, 31)]

timmy = Turtle()
timmy.hideturtle()
timmy.speed('fastest')
timmy.penup()
colormode(255)
x = -230
y = -220
timmy.teleport(x, y)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(rgb_list))
        timmy.forward(50)

    y += 50
    timmy.goto(x, y)

screen = Screen()
screen.exitonclick()
