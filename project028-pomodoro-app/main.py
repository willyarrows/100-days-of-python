import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

POMODORO = 4

timer = None
repetition = 1


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global repetition

    repetition = 1
    canvas.itemconfig(timer_text, text=f"00:00")
    label_checkmark.config(text="✓")
    label_title.config(text="Timer", fg=GREEN, font=(FONT_NAME, 38, "bold"), pady=5)
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetition

    work_min_sec = int(WORK_MIN*60)
    short_break_sec = int(SHORT_BREAK_MIN*60)
    long_break_sec = int(LONG_BREAK_MIN*60)

    if repetition <= POMODORO*2:
        print(repetition)
        if repetition == POMODORO*2:
            label_title.config(text="Break", fg=RED, font=(FONT_NAME, 38, "bold"))
            count_down(long_break_sec)
        elif repetition % 2 != 0:
            label_title.config(text="Work", fg=GREEN, font=(FONT_NAME, 38, "bold"))
            count_down(work_min_sec)
            if repetition != 1:
                label_checkmark.config(text=label_checkmark.cget("text")+"✓")
        elif repetition % 2 == 0:
            label_title.config(text="Break", fg=PINK, font=(FONT_NAME, 38, "bold"))
            count_down(short_break_sec)

        repetition += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    mm = str(count // 60).zfill(2)
    ss = str(count % 60).zfill(2)
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label_title = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 38), pady=5)
label_title.grid(row=0, column=1)

label_checkmark = tk.Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
label_checkmark.grid(row=3, column=1)

button_start = tk.Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = tk.Button(text="Reset", command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
