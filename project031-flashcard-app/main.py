import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 20, "italic")
WORD_FONT = ("Ariel", 40, "bold")

try:
    dict_words = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    dict_words = pd.read_csv("data/french_words.csv").to_dict(orient="records")

dict_french = {words['French']: words['English'] for words in dict_words if len(words) > 0}

current_card = []
flash_card_timer = None


# ---------------------------- GUESS LOGIC ---------------------------- #

def generate_random_card():
    global current_card

    french_word = random.choice(list(dict_french.keys()))
    english_word = dict_french[french_word]

    current_card = [french_word, english_word]


def display_new_card():
    global flash_card_timer, current_card

    generate_random_card()
    canvas.itemconfig(canvas_image, image=front_card_img)
    canvas.itemconfig(text_language, text="French", fill="black")
    canvas.itemconfig(text_word, text=current_card[0], fill="black")
    flash_card_timer = window.after(3000, flip_card, current_card)


def flip_card(card):
    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(text_language, text="English", fill="white")
    canvas.itemconfig(text_word, text=card[1], fill="white")


def correct_guess():
    global flash_card_timer, current_card

    window.after_cancel(flash_card_timer)

    dict_french.pop(current_card[0])
    df_words_to_learn = pd.DataFrame.from_dict(dict_french, orient='index', columns=['English'])
    df_words_to_learn.to_csv("./data/words_to_learn.csv", index_label='French')

    display_new_card()


def wrong_guess():
    global flash_card_timer

    window.after_cancel(flash_card_timer)
    display_new_card()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg="#B1DDC6")

canvas = tk.Canvas(width=600, height=300, bg="#B1DDC6", highlightthickness=0)
front_card_img = tk.PhotoImage(file="./images/card_front.png")
back_card_img = tk.PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(300, 150, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

text_language = canvas.create_text(300, 75, text="French", font=LANGUAGE_FONT)
text_word = canvas.create_text(300, 150, text="Trouve", font=WORD_FONT)

correct_img = tk.PhotoImage(file="./images/right.png")
button_correct = tk.Button(image=correct_img, command=correct_guess, highlightthickness=0)
button_correct.grid(row=1, column=0, padx=10, pady=15)

wrong_img = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(image=wrong_img, command=wrong_guess, highlightthickness=0)
button_wrong.grid(row=1, column=1, padx=10, pady=15)

display_new_card()

window.mainloop()
