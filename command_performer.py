# command_performer.py

import pyautogui
import webbrowser
from responder import respond
from gpt4all import GPT4All
from config import GPT4ALL_MODEL_PATH

model = GPT4All(GPT4ALL_MODEL_PATH, allow_download=False)
listening_to_task = False
asking_a_question = False

def perform_command(command):
    global listening_to_task
    global asking_a_question
    global listening_for_trigger_word

    if not command:
        listening_for_trigger_word = True
        return False

    print("Command: ", command)

    if "take a screenshot" in command:
        take_screenshot()
    elif "ask a question" in command:
        ask_question()
    elif asking_a_question:
        process_question(command)
    elif "exit" in command:
        return True  # Return True if the exit command is received
    else:
        respond("Sorry, I'm not sure how to handle that command.")

    listening_for_trigger_word = True
    return False  # Return False for all other commands

def take_screenshot():
    try:
        pyautogui.screenshot("screenshot.png")
        respond("I took a screenshot for you.")
    except Exception as e:
        respond(f"Failed to take screenshot: {e}")

def ask_question():
    global asking_a_question
    asking_a_question = True
    respond("What's your question?")

def process_question(command):
    global asking_a_question
    asking_a_question = False
    respond("Thinking...")
    print("User command: ", command)
    try:
        output = model.generate(command, max_tokens=200)
        print("Output: ", output)
        respond(output)
    except Exception as e:
        respond(f"Failed to generate response: {e}")
