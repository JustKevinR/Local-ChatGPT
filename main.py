# main.py
import sounddevice as sd
from recognizer import listen_for_command
from responder import respond
from event_handler import handle_special_event, special_event_occurred
from command_performer import perform_command
import time
import keyboard

# Global flag to determine input method
use_keyboard_input = True  # Set to False to use microphone input

def main():
    listening_for_trigger_word = True

    while True:
        if special_event_occurred():
            handle_special_event()
            # toggle_input_method()
        else:
            if use_keyboard_input:
                text_input = input("Enter command: ").strip()
            else:
                text_input = listen_for_command()

            if text_input:
                exit_command_received = perform_command(text_input)
                if exit_command_received:  # Check if exit command was received
                    break

        time.sleep(1)

    respond("Goodbye.")

if __name__ == "__main__":
    main()
