import tkinter as tk
import tkinter.messagebox
import csv
import random
import pyperclip

DEFAULT_USERNAME = "willy.sebastian@gmail.com"
LETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
SYMBOLS = ('!', '#', '$', '%', '&', '(', ')', '*', '+')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letter = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(4, 6))]
    password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(4, 6))]

    password_combination = password_letter + password_symbols + password_numbers
    random.shuffle(password_combination)

    generated_password = "".join(password_combination)
    entry_password.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if website.strip() == "" or username.strip() == "" or password.strip() == "":
        tk.messagebox.showerror(title="Error", message="All fields must not be empty")
    else:
        confirmation_message = (f"These are the details entered, "
                                f"\nEmail : {username} "
                                f"\nPassword : {password} "
                                f"\nIs it ok to save ?")

        is_ok = tk.messagebox.askokcancel(title=website, message=confirmation_message)

        if is_ok:
            data = [website, username, password]

            try:
                with open("password_list.csv", mode="a", newline='') as output_file:
                    csv.writer(output_file, delimiter="|").writerow(data)

                    tk.messagebox.showinfo(title=website, message="Username and Password has been saved")

                    entry_website.delete(0, tk.END)
                    entry_username.delete(0, tk.END)
                    entry_password.delete(0, tk.END)

                    entry_website.focus()
                    entry_username.insert(0, DEFAULT_USERNAME)

            except Exception as err:
                tk.messagebox.showerror(message=err)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=35, pady=35)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website
tk.Label(text="Website : ").grid(sticky=tk.W, row=1, column=0)
entry_website = tk.Entry(width=55)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

# Username
tk.Label(text="Email / Username : ").grid(sticky=tk.W, row=2, column=0)
entry_username = tk.Entry(width=55)
entry_username.insert(0, DEFAULT_USERNAME)
entry_username.grid(row=2, column=1, columnspan=2)

# Password
tk.Label(text="Password : ").grid(sticky=tk.W, row=3, column=0)
entry_password = tk.Entry(width=36)
entry_password.grid(row=3, column=1)

button_gen_password = tk.Button(text="Generate Password", command=generate_password)
button_gen_password.grid(row=3, column=2)

button_add = tk.Button(text="Add", width=46, command=save_password)
button_add.grid(row=4, column=1, columnspan=2, sticky=tk.E)

window.mainloop()
