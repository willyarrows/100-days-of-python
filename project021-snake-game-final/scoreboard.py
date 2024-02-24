from turtle import Turtle

SCORE_FONT = ('Courier', 12, 'normal')
SCORE_ALIGNMENT = 'center'

GAME_OVER_FONT = ('Courier', 20, 'normal')
GAME_OVER_ALIGNMENT = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.fetch_high_score()

        self.color('white')
        self.speed('fastest')
        self.penup()

        x_pos, y_pos = (0, 250)
        self.goto(x_pos, y_pos)

        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.clear()
        display = f"Score: {self.score}   High Score : {self.high_score}"
        self.write(arg=display, align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        display = f"GAME OVER"
        self.home()
        self.write(arg=display, align=GAME_OVER_ALIGNMENT, font=GAME_OVER_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

        self.display_score()
        self.save_high_score()

    def fetch_high_score(self):
        with open("high_score.txt") as file:
            high_score = file.read()

        self.high_score = int(high_score)

    def save_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
