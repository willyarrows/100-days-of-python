import turtle
import pandas as pd

CHECKER_FONT = ("Arial", 9, "normal")

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

checker = turtle.Turtle()
checker.shapesize(0.4, 0.4)
checker.penup()

score = 0
is_game_on = True
df_states = pd.read_csv("50_states.csv")
correct_answer = []
while is_game_on:
    if score == 0:
        title = "Guess the State"
        prompt = "Guess U.S. State Name : "
    else:
        title = f" {score}/50 States Correct"
        prompt = "What's another state's name ? "

    answer_state = screen.textinput(title=title, prompt=prompt).title()
    if answer_state.lower() == "exit":
        is_game_on = False
    else:
        state = df_states[df_states.state == answer_state]
        if not state.empty:
            # state_coordinate = (state.x.iloc[0], state.y.iloc[0])
            state_coordinate = (int(state.x), int(state.y))
            checker.goto(state_coordinate)
            checker.write(arg=answer_state, align='center', font=CHECKER_FONT)
            if answer_state not in correct_answer:
                correct_answer.append(answer_state)
                score += 1

screen.exitonclick()
