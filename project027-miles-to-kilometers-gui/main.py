import tkinter as tk


def calculate_button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_output.config(text=f"{km:.3f}")


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(300, 200)
window.config(padx=50, pady=50)

# Move window to center
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x, y))

# Input Section
miles_input = tk.Entry()
miles_input.insert(tk.END, "0")
miles_input.config(width=10)
miles_input.grid(row=0, column=1)

tk.Label(text="Miles").grid(row=0, column=2)

# Output Section
tk.Label(text="is equal to").grid(row=1, column=0)
tk.Label(text="Km").grid(row=1, column=2)

km_output = tk.Label(text="0")
km_output.grid(row=1, column=1)

# Button Section
calculate_button = tk.Button(text="Calculate", command=calculate_button_clicked)
calculate_button.grid(row=2, column=1)

window.mainloop()

