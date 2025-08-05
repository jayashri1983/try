import os

def run_ping(user_input):
    # 🚨 Vulnerable: unsanitized input leads to command injection
    command = f"ping -c 1 {user_input}"
    os.system(command)

if __name__ == "__main__":
    user_input = input("Enter IP address or hostname: ")
    run_ping(user_input)
import subprocess

def run_command():
    user_input = input("Enter command: ")
    subprocess.call(user_input, shell=True)  # 🚨 vulnerable
