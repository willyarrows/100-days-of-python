import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("arial", 15, "italic")


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.label_score = tk.Label(text="Score: 0")
        self.label_score.grid(row=0, column=1)
        self.label_score.config(bg=THEME_COLOR, fg='white', padx=20, pady=20)

        self.canvas = tk.Canvas(width=300, height=300, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 150, width=280, fill="black", font=QUESTION_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = tk.PhotoImage(file="./images/true.png")
        self.button_true = tk.Button(image=true_img, command=self.guess_true, highlightthickness=0)
        self.button_true.grid(row=2, column=0, padx=20, pady=20)

        false_img = tk.PhotoImage(file="./images/false.png")
        self.button_false = tk.Button(image=false_img, command=self.guess_false, highlightthickness=0)
        self.button_false.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz !!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def guess_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.label_score.config(text=f"Score: {self.quiz.score}")

    def guess_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.label_score.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')

        self.window.after(1000, self.get_next_question)
