import tkinter as tk

THEME_COLOR = "#375362"
QUESTION_FONT = ("arial", 15, "italic")

class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.label_score = tk.Label(text="Score: 0")
        self.label_score.grid(row=0, column=1)
        self.label_score.config(bg=THEME_COLOR, fg='white', padx=20, pady=20)

        self.canvas = tk.Canvas(width=300, height=300, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 150, text="Question 1", fill="black", font=QUESTION_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = tk.PhotoImage(file="./images/true.png")
        self.button_true = tk.Button(image=true_img, command=self.guess_true, highlightthickness=0)
        self.button_true.grid(row=2, column=0, padx=20, pady=20)

        false_img = tk.PhotoImage(file="./images/false.png")
        self.button_false = tk.Button(image=false_img, command=self.guess_false, highlightthickness=0)
        self.button_false.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()

    def guess_true(self):
        pass

    def guess_false(self):
        pass
