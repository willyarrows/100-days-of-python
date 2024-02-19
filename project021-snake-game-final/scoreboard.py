from turtle import Turtle

SCORE_FONT = ('Courier', 12, 'normal')
SCORE_ALIGNMENT = 'center'

GAME_OVER_FONT = ('Courier', 20, 'normal')
GAME_OVER_ALIGNMENT = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.speed('fastest')
        self.penup()

        x_pos, y_pos = (0, 250)
        self.goto(x_pos, y_pos)

        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.clear()
        display = f"Score: {self.score}"
        self.write(arg=display, align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        display = f"GAME OVER"
        self.home()
        self.write(arg=display, align=GAME_OVER_ALIGNMENT, font=GAME_OVER_FONT)
