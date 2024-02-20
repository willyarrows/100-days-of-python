from turtle import Turtle

SCORE_FONT = ('Courier', 30, 'bold')
SCORE_ALIGNMENT = 'center'


class ScoreBoard(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.l_score = 0
        self.r_score = 0

        self.create_score_board()
        self.display_score()

    def create_score_board(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        x_pos = 0
        y_pos = self.screen.window_height() / 2 - 60
        self.goto(x_pos, y_pos)

    def display_score(self):
        self.clear()
        display = f"{self.l_score}   :   {self.r_score}"
        self.write(arg=display, align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def increase_score(self, player):
        if player == 'left':
            self.l_score += 1
        elif player == 'right':
            self.r_score += 1

        self.display_score()
