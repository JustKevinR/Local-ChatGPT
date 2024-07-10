# event_handler.py
import threading
from recognizer import listen_for_command
from command_performer import perform_command

def special_event_occurred():
    # Replace with actual condition to detect the event
    return False

def handle_special_event():
    command = listen_for_command()
    if command:
        perform_command(command)
