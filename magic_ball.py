"""Magic Fortune Ball — ask a yes/no question and let the stars answer. 🔮✨

Just for fun! Pure tkinter — no extra libraries.
"""

import random
import tkinter as tk

BG = "#2b1055"
BALL = "#6a3cbc"
TEXT = "#ffffff"
GLOW = "#ffd6f5"

ANSWERS = [
    ("Yes, absolutely! 💖", "#ff8ad8"),
    ("For sure! ✨", "#ffb3e6"),
    ("The stars say YES 🌟", "#ffc2f0"),
    ("Hmm... maybe 🤔", "#c9a7ff"),
    ("Ask again later 🌙", "#a78bfa"),
    ("I'm not so sure 😶", "#b0a0e6"),
    ("Probably not 🙈", "#88a7ff"),
    ("No way! 🚫", "#ff9db0"),
    ("Only if you believe 🦄", "#9ef0ff"),
    ("Definitely! Go for it! 🚀", "#9effc2"),
]

root = tk.Tk()
root.title("🔮 Magic Fortune Ball ✨")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(root, text="🔮 MAGIC FORTUNE BALL ✨", bg=BG, fg=GLOW,
         font=("Comic Sans MS", 18, "bold")).pack(pady=(18, 4))
tk.Label(root, text="ask a yes / no question, then shake the ball!",
         bg=BG, fg=TEXT, font=("Comic Sans MS", 10)).pack(pady=(0, 12))

question = tk.Entry(root, width=34, bg="#3d2170", fg=TEXT,
                    insertbackground=GLOW, font=("Comic Sans MS", 13),
                    relief="flat", justify="center")
question.pack(ipady=8, padx=24, pady=(0, 16))
question.insert(0, "Will today be awesome?")

ball = tk.Canvas(root, width=240, height=240, bg=BG, highlightthickness=0)
ball.pack()
ball.create_oval(20, 20, 220, 220, fill=BALL, outline=GLOW, width=4)
answer_text = ball.create_text(120, 120, text="🔮", fill=TEXT,
                               font=("Comic Sans MS", 40), width=180,
                               justify="center")

def shake(times=6):
    if times > 0:
        label, color = random.choice(ANSWERS)
        ball.itemconfig(answer_text, text="✨", fill=color,
                        font=("Comic Sans MS", 40))
        root.after(90, lambda: shake(times - 1))
    else:
        label, color = random.choice(ANSWERS)
        ball.itemconfig(answer_text, text=label, fill=color,
                        font=("Comic Sans MS", 16, "bold"))

tk.Button(root, text="✨ SHAKE THE BALL ✨", command=lambda: shake(),
          bg=GLOW, fg=BG, activebackground="#ff8ad8",
          font=("Comic Sans MS", 14, "bold"), relief="flat", bd=0,
          padx=18, pady=10, cursor="star").pack(pady=16)

root.mainloop()
