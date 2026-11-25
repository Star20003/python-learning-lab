import random
import tkinter as tk

DEMO_PASSWORD = "NEON-404"
AUTHORIZED_USER = "STELLA#054?056"
ACTIVE_USER = AUTHORIZED_USER
GREEN, DIM_GREEN, RED, BACKGROUND = "#00ff66", "#006b2b", "#ff244a", "#030504"

root = tk.Tk()
root.title("BLACKOUT PROTOCOL — DEMO")
root.configure(bg=BACKGROUND)
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())

canvas = tk.Canvas(root, bg=BACKGROUND, highlightthickness=0)
canvas.place(relwidth=1, relheight=1)
root.update_idletasks()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()

# Decorative effects only: this program never touches the network or system.
columns = [(x, random.randint(-height, 0), random.randint(14, 28))
           for x in range(8, width, 18)]

def matrix_rain():
    canvas.delete("rain")
    for index, (x, y, speed) in enumerate(columns):
        trail = "".join(random.choice("01ABCDEF#$%") for _ in range(8))
        canvas.create_text(x, y, text=trail, anchor="n", fill=DIM_GREEN,
                           font=("Consolas", 10), tags="rain")
        canvas.create_text(x, y + 22, text=random.choice("01#@"), anchor="n",
                           fill=GREEN, font=("Consolas", 12, "bold"), tags="rain")
        y += speed
        if y > height + 100:
            y = random.randint(-180, -30)
        columns[index] = (x, y, speed)
    root.after(70, matrix_rain)

scan_y = 0
def scan_line():
    global scan_y
    canvas.delete("scan")
    canvas.create_line(0, scan_y, width, scan_y, fill="#075e29", width=2, tags="scan")
    scan_y = (scan_y + 5) % height
    root.after(25, scan_line)

panel = tk.Frame(root, bg="#07120b", highlightbackground=GREEN, highlightthickness=1)
panel.place(relx=0.5, rely=0.5, anchor="center", width=760, height=520)
tk.Label(panel, text="BLACKOUT  //  PROTOCOL", fg=GREEN, bg="#07120b",
         font=("Consolas", 13, "bold")).pack(pady=(18, 2))
title = tk.Label(panel, text="SYSTEM COMPROMISED", fg=RED, bg="#07120b",
                 font=("Consolas", 32, "bold"))
title.pack(pady=(15, 8))
message = tk.Label(panel, text="YOUR DISPLAY HAS BEEN LOCKED", fg="white", bg="#07120b",
                   font=("Consolas", 18))
message.pack()
status = tk.Label(panel, text="[ SIMULATION ACTIVE ]", fg="#b4ffc9",
                  bg="#07120b", font=("Consolas", 10, "bold"))
status.pack(pady=(8, 12))
log = tk.Label(panel, justify="left", anchor="w", width=66, height=5, fg="#89ffae",
               bg="#020402", font=("Consolas", 10))
log.pack(padx=35, pady=(0, 14), fill="x")
question = tk.Label(panel, text="ENTER DEMO PASSWORD:", fg=GREEN, bg="#07120b",
                    font=("Consolas", 16, "bold"))
question.pack(pady=(0, 8))
password_entry = tk.Entry(panel, show="*", font=("Consolas", 20), bg="#020402",
                          fg=GREEN, insertbackground="white", justify="center",
                          relief="flat", width=24)
password_entry.pack(ipady=7)
result = tk.Label(panel, text="", fg="white", bg="#07120b", font=("Consolas", 17, "bold"))
result.pack(pady=12)

def update_logs():
    lines = [
        f"> TRACE ROUTE: 10.{random.randint(10, 99)}.{random.randint(10, 99)}.██",
        f"> CIPHER STATUS: {random.choice(['AES-256', 'SHA-512', 'QUANTUM-LINK'])}",
        f"> PACKET STREAM: {random.randint(1200, 9999)} KB/s",
        f"> FIREWALL: {random.choice(['BYPASSED', 'ANALYZING', 'MASKED'])}",
        "> AWAITING AUTHORIZATION...",
    ]
    log.config(text="\n".join(lines))
    root.after(850, update_logs)

def glitch():
    title.config(text=random.choice(["SYSTEM COMPROMISED", "SYST3M C0MPR0MISED", "SYSTEM COMPROMISED"]))
    root.after(180, glitch)

def check_password(event=None):
    if ACTIVE_USER == AUTHORIZED_USER and password_entry.get() == DEMO_PASSWORD:
        result.config(text="ACCESS GRANTED!", fg=GREEN)
        message.config(text="SYSTEM RESTORED", fg=GREEN)
        question.config(text="MISSION COMPLETE!")
        status.config(text="[ DEMO COMPLETE — CLOSING SAFELY ]")
        password_entry.pack_forget()
        submit_button.pack_forget()
        root.after(3500, root.destroy)
    else:
        result.config(text="IDENTITY OR PASSWORD DENIED!", fg=RED)
        password_entry.delete(0, tk.END)
        panel.config(highlightbackground=RED)
        root.after(220, lambda: panel.config(highlightbackground=GREEN))

submit_button = tk.Button(panel, text="UNLOCK SYSTEM", command=check_password,
                          font=("Consolas", 14, "bold"), bg="#10351d", fg=GREEN,
                          activebackground="#1a5c2e", activeforeground="white",
                          relief="flat", padx=25, pady=8)
submit_button.pack()

root.bind("<Return>", check_password)
root.focus_force()
password_entry.focus_set()
matrix_rain()
scan_line()
update_logs()
glitch()
root.mainloop()
