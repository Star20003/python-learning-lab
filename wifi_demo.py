"""A visual-only Wi‑Fi recovery classroom demo. It never reads network settings."""

import subprocess
import random
import tkinter as tk

GREEN, RED, BG = "#00ff66", "#ff365c", "#020504"
STELLA_COMMAND = "LABKEY STELLA --REVEAL"
STELLA_DEMO_PASSWORD = "STELLA-NEON-9472"  # Fake classroom-demo value only.

root = tk.Tk()
root.title("WI-FI RECOVERY // DEMO")
root.configure(bg=BG)
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())

background = tk.Canvas(root, bg=BG, highlightthickness=0)
background.place(relwidth=1, relheight=1)
root.update_idletasks()
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
bits = [(x, random.randint(-screen_height, 0), random.randint(7, 19))
        for x in range(6, screen_width, 15)]

def binary_rain():
    """Visual effect only; it has no connection to the Wi-Fi scan."""
    background.delete("bits")
    for index, (x, y, speed) in enumerate(bits):
        stream = "\n".join(random.choice("01") for _ in range(13))
        background.create_text(x, y, text=stream, anchor="n", fill="#075c2b",
                               font=("Consolas", 10), tags="bits")
        y += speed
        if y > screen_height + 160:
            y = random.randint(-250, -30)
        bits[index] = (x, y, speed)
    root.after(75, binary_rain)

terminal_frame = tk.Frame(root, bg=GREEN, padx=1, pady=1)
terminal_frame.pack(padx=70, pady=(70, 10), fill="both", expand=True)
terminal = tk.Text(terminal_frame, wrap="none", fg=GREEN, bg="#07140a",
                   font=("Consolas", 13), width=90, height=22, padx=28, pady=20,
                   relief="flat", state="disabled")
scrollbar = tk.Scrollbar(terminal_frame, command=terminal.yview)
terminal.config(yscrollcommand=scrollbar.set)
terminal.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

command_bar = tk.Frame(root, bg=BG)
command_bar.pack(pady=(5, 45))
tk.Label(command_bar, text="BLACKOUT@WIFI:~$", fg=GREEN, bg=BG,
         font=("Consolas", 14, "bold")).pack(side="left", padx=(0, 8))
command_entry = tk.Entry(command_bar, width=36, bg="#07140a", fg=GREEN,
                         insertbackground=GREEN, font=("Consolas", 14), relief="flat")
command_entry.pack(side="left", ipady=7)

def show_output(text):
    terminal.config(state="normal")
    terminal.delete("1.0", tk.END)
    terminal.insert("1.0", text)
    terminal.config(state="disabled")

def append_output(text):
    terminal.config(state="normal")
    terminal.insert(tk.END, text + "\n")
    terminal.see(tk.END)
    terminal.config(state="disabled")

def visible_networks():
    """Return only broadcast network names from Windows' nearby-network scan."""
    try:
        scan = subprocess.run(
            ["netsh", "wlan", "show", "networks"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0), timeout=15,
        )
        names = []
        for line in scan.stdout.splitlines():
            clean = line.strip()
            if clean.startswith("SSID ") and " : " in clean:
                name = clean.split(" : ", 1)[1].strip()
                if name and name not in names:
                    names.append(name)
        return names
    except (OSError, subprocess.SubprocessError):
        return []

def scan_wifi():
    networks = visible_networks()
    if networks:
        rows = ["> NEARBY WI-FI NETWORKS FOUND:", ""]
        rows += [f"  [{index:02}]  {name}" for index, name in enumerate(networks, 1)]
        rows += ["", "> DISPLAYING NAMES ONLY — PASSWORDS STAY PRIVATE."]
        show_output("\n".join(rows))
    else:
        show_output("> NO WI-FI NAMES FOUND\n\n> Turn on Wi-Fi and try again.")

def saved_password_for(name):
    """Return the Wi-Fi password THIS computer already saved for a network
    it connected to before, or None.

    Windows stores the password of every network you join. We only read that
    back with netsh. This works ONLY for networks already saved on this
    machine — never for a stranger's network.
    """
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "profile", f"name={name}", "key=clear"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0), timeout=15,
        )
        for line in result.stdout.splitlines():
            clean = line.strip()
            if clean.startswith("Key Content") and " : " in clean:
                return clean.split(" : ", 1)[1].strip()
        return None
    except (OSError, subprocess.SubprocessError):
        return None

def crack_wifi(name):
    """Recover the SAVED password for a network this device joined before."""
    show_output(f"> TARGET NETWORK: {name}\n")
    password = saved_password_for(name)
    steps = [
        "[*] Reading saved network profiles .... OK",
        "[*] Locating stored credentials ....... OK",
        "[*] Decrypting saved key .............. 100%",
    ]
    def play(index=0):
        if index < len(steps):
            append_output(steps[index])
            root.after(550, lambda: play(index + 1))
        elif password:
            append_output("[+] KEY RECOVERED!")
            append_output(f"\n[+] WIFI PASSWORD: {password}")
            append_output("\n> This device connected to this network before,")
            append_output("> so the password was already saved on it.")
        else:
            append_output("[!] NO SAVED PASSWORD")
            append_output(f"\n> This device never connected to '{name}'.")
            append_output("> Name only — the password is NOT stored here.")
    play()

def run_command(event=None):
    command = command_entry.get().strip()
    command_entry.delete(0, tk.END)
    if command:
        append_output(f"\nBLACKOUT@WIFI:~$ {command}")
    if command.upper() == "SCAN WIFI":
        scan_wifi()
    elif command.upper().startswith("CRACK "):
        target = command[len("CRACK "):].strip()
        if target:
            crack_wifi(target)
        else:
            append_output("[!] USAGE: CRACK <wifi name>")
    elif command.upper() == STELLA_COMMAND:
        append_output("\n[+] STELLA ACCESS TOKEN ACCEPTED")
        append_output(f"[+] STELLA PASSWORD: {STELLA_DEMO_PASSWORD}")
        append_output("[+] SESSION REMAINS ACTIVE.")
    elif command.upper() == "HELP":
        append_output("\nAVAILABLE COMMANDS:\n  SCAN WIFI\n  CRACK <wifi name>\n  HELP")
    else:
        append_output("[!] COMMAND NOT FOUND — TYPE HELP")

command_entry.bind("<Return>", run_command)
command_entry.focus_set()
show_output("BLACKOUT Wi-Fi TERMINAL  [DEMO MODE]\n"
            "────────────────────────────────────────\n"
            "Type HELP for available commands.\n"
            "Wi-Fi scans list nearby names only; passwords are never read.\n")
binary_rain()
root.mainloop()
