from turtle import Turtle

FONT = ("Courier", 20, "normal")
GAME_OVER = "Game Over !!!"
SCORE_POSITION = (-280, 225)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.display_level()

    @staticmethod
    def game_over():
        writer = Turtle()
        writer.color('black')
        writer.penup()
        writer.write(arg=GAME_OVER, align='center', font=FONT)

    def display_level(self):
        self.clear()
        display_text = f"Level : {self.level}"
        self.write(arg=display_text, align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.display_level()
