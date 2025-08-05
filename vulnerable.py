import os

def run_command():
    user_input = input("Enter command: ")
    subprocess.call(user_input, shell=True)  # 🚨 vulnerable
