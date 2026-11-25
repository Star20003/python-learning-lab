"""A cute, sparkly pastel calculator for the classroom. 🌸

Pure tkinter — no extra libraries. Works on Windows, Mac and Linux.
"""

import tkinter as tk

PINK_BG = "#ffe4ef"
DISPLAY_BG = "#fff0f7"
NUM_BG = "#ffd1e3"
OP_BG = "#ffb3d1"
EQUAL_BG = "#ff7eb6"
CLEAR_BG = "#c9a7ff"
TEXT = "#6b2d5c"

root = tk.Tk()
root.title("🌸 Sparkle Calculator 🌸")
root.configure(bg=PINK_BG)
root.resizable(False, False)

expression = ""
display_var = tk.StringVar(value="0")

def refresh():
    display_var.set(expression if expression else "0")

def press(symbol):
    global expression
    expression += symbol
    refresh()

def clear_all():
    global expression
    expression = ""
    refresh()

def backspace():
    global expression
    expression = expression[:-1]
    refresh()

def calculate():
    global expression
    allowed = set("0123456789.+-*/() ")
    if expression and set(expression) <= allowed:
        try:
            result = eval(expression, {"__builtins__": {}}, {})  # only math, no names
            expression = str(result)
        except (SyntaxError, ZeroDivisionError, ValueError):
            expression = ""
            display_var.set("oops! 🙈 try again")
            return
    refresh()

title = tk.Label(root, text="✨ My Sparkle Calc ✨", bg=PINK_BG, fg=TEXT,
                 font=("Comic Sans MS", 18, "bold"))
title.grid(row=0, column=0, columnspan=4, pady=(16, 8))

display = tk.Label(root, textvariable=display_var, bg=DISPLAY_BG, fg=TEXT,
                   font=("Comic Sans MS", 24, "bold"), anchor="e",
                   width=12, padx=14, pady=16, relief="flat")
display.grid(row=1, column=0, columnspan=4, padx=16, pady=8, sticky="we")

# (label, row, col, background, command)
buttons = [
    ("C", 2, 0, CLEAR_BG, clear_all),
    ("⌫", 2, 1, CLEAR_BG, backspace),
    ("(", 2, 2, OP_BG, lambda: press("(")),
    (")", 2, 3, OP_BG, lambda: press(")")),
    ("7", 3, 0, NUM_BG, lambda: press("7")),
    ("8", 3, 1, NUM_BG, lambda: press("8")),
    ("9", 3, 2, NUM_BG, lambda: press("9")),
    ("÷", 3, 3, OP_BG, lambda: press("/")),
    ("4", 4, 0, NUM_BG, lambda: press("4")),
    ("5", 4, 1, NUM_BG, lambda: press("5")),
    ("6", 4, 2, NUM_BG, lambda: press("6")),
    ("×", 4, 3, OP_BG, lambda: press("*")),
    ("1", 5, 0, NUM_BG, lambda: press("1")),
    ("2", 5, 1, NUM_BG, lambda: press("2")),
    ("3", 5, 2, NUM_BG, lambda: press("3")),
    ("−", 5, 3, OP_BG, lambda: press("-")),
    ("0", 6, 0, NUM_BG, lambda: press("0")),
    (".", 6, 1, NUM_BG, lambda: press(".")),
    ("+", 6, 2, OP_BG, lambda: press("+")),
    ("=", 6, 3, EQUAL_BG, calculate),
]

for label, row, col, color, command in buttons:
    tk.Button(root, text=label, command=command, bg=color, fg=TEXT,
              activebackground=EQUAL_BG, font=("Comic Sans MS", 16, "bold"),
              width=4, height=1, relief="flat", bd=0, cursor="heart"
              ).grid(row=row, column=col, padx=6, pady=6, ipady=6)

footer = tk.Label(root, text="made with 💖", bg=PINK_BG, fg=TEXT,
                  font=("Comic Sans MS", 10))
footer.grid(row=7, column=0, columnspan=4, pady=(4, 14))

root.mainloop()
