import subprocess
import sys


AUTHORIZED_CODENAME = "STELLA#054?056"

username = input("ENTER YOUR CODENAME: ")

if username != AUTHORIZED_CODENAME:
    print("ERROR: IDENTITY NOT RECOGNIZED.")
    print("ACCESS DENIED.")
    sys.exit(1)

print("IDENTITY VERIFIED...")
input("PRESS ENTER TO INITIATE...")

subprocess.Popen([sys.executable, "blackout.py"])
