"""Secret Message Maker — a cute + hacker toy to send coded notes. 🔐🌸

It uses a Caesar cipher: every letter is shifted by a secret number (the key).
Your friend needs the SAME key to read the message back. Great for passing
secret notes! Pure tkinter — no extra libraries.
"""

import tkinter as tk

BG = "#1b1033"          # deep purple night
PANEL = "#2a1b4d"
NEON = "#ff5fd2"        # neon pink
MINT = "#5ffbd0"        # neon mint
TEXT = "#f3e9ff"

def shift_text(text, key):
    """Shift every letter by `key`. Non-letters stay the same."""
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - 65 + key) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - 97 + key) % 26 + 97))
        else:
            result.append(char)
    return "".join(result)

root = tk.Tk()
root.title("🔐 Secret Message Maker 🌸")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(root, text="✦ SECRET MESSAGE MAKER ✦", bg=BG, fg=NEON,
         font=("Consolas", 18, "bold")).pack(pady=(18, 4))
tk.Label(root, text="type a message, pick a secret key, and scramble it!",
         bg=BG, fg=TEXT, font=("Consolas", 10)).pack(pady=(0, 12))

tk.Label(root, text="Your message:", bg=BG, fg=MINT,
         font=("Consolas", 11, "bold")).pack(anchor="w", padx=24)
input_box = tk.Text(root, height=4, width=42, bg=PANEL, fg=TEXT,
                    insertbackground=NEON, font=("Consolas", 12),
                    relief="flat", padx=12, pady=10, wrap="word")
input_box.pack(padx=24, pady=(4, 12))

key_row = tk.Frame(root, bg=BG)
key_row.pack(pady=(0, 10))
tk.Label(key_row, text="🔑 Secret key:", bg=BG, fg=MINT,
         font=("Consolas", 11, "bold")).pack(side="left", padx=(0, 8))
key_var = tk.IntVar(value=3)
tk.Spinbox(key_row, from_=1, to=25, textvariable=key_var, width=4,
           bg=PANEL, fg=TEXT, font=("Consolas", 12), relief="flat",
           buttonbackground=NEON, justify="center").pack(side="left")

output_box = tk.Text(root, height=4, width=42, bg="#120a26", fg=MINT,
                     font=("Consolas", 12, "bold"), relief="flat",
                     padx=12, pady=10, wrap="word", state="disabled")

def show_result(text):
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert("1.0", text)
    output_box.config(state="disabled")

def encode():
    message = input_box.get("1.0", tk.END).rstrip("\n")
    show_result(shift_text(message, key_var.get()))

def decode():
    message = input_box.get("1.0", tk.END).rstrip("\n")
    show_result(shift_text(message, -key_var.get()))

button_row = tk.Frame(root, bg=BG)
button_row.pack(pady=(4, 10))
tk.Button(button_row, text="🔒 SCRAMBLE", command=encode, bg=NEON, fg=BG,
          activebackground=MINT, font=("Consolas", 13, "bold"),
          relief="flat", bd=0, padx=14, pady=8).pack(side="left", padx=8)
tk.Button(button_row, text="🔓 UNSCRAMBLE", command=decode, bg=MINT, fg=BG,
          activebackground=NEON, font=("Consolas", 13, "bold"),
          relief="flat", bd=0, padx=14, pady=8).pack(side="left", padx=8)

tk.Label(root, text="Result:", bg=BG, fg=MINT,
         font=("Consolas", 11, "bold")).pack(anchor="w", padx=24)
output_box.pack(padx=24, pady=(4, 18))

root.mainloop()
