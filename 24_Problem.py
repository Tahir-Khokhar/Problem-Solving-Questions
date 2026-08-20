# 24. Simple log generator script.

# Problem: Write a function that appends a timestamped message to a log file.

from datetime import datetime

def log_message(message, filepath="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, 'a') as file:
        file.write(f"[{timestamp}] {message}\n")

log_message("System started", "app.log")
log_message("Task completed", "app.log")
print("Logged messages to app.log")
