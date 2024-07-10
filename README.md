# Local-ChatGPT
Python application that allows users to interact offline with an AI assistant using voice commands or keyboard inpu

1. config.py: This file contains configuration settings, such as the paths to the GPT4All and Whisper models, and a set of allowed characters for text-to-speech output.

2. recognizer.py: This module handles speech recognition using the speech_recognition and whisper libraries. It provides a listen_for_command function that listens for audio input from the microphone, transcribes it using the Whisper model, and returns the transcribed text.

3. responder.py: This module is responsible for text-to-speech output. It uses the pyttsx3 library on non-macOS systems and the say command on macOS to speak the provided text.

4.command_performer.py: This module processes the user's commands. It includes functions to take screenshots, ask questions, and generate responses using the GPT4All model. The perform_command function is the main entry point for handling user commands.

5. event_handler.py: This module seems to be intended for handling special events, although the provided code doesn't implement any specific event handling logic.

6. main.py: This is the main entry point of the application. It sets up a loop that listens for user input (either from the microphone or the keyboard), processes the input using perform_command, and handles any special events that may occur.


Requirements

pip install these:
pyaudio
SpeechRecognition
whisper (from the OpenAI GitHub repository)
pyautogui
pyttsx3
gpt4all
sounddevice

config.py file:

Whisper Base Model: You'll need to download the Whisper base model and specify its path in the BASE_MODEL_PATH variable in config.py.
GPT4All Model: You'll need to download the GPT4All model and specify its path in the GPT4ALL_MODEL_PATH variable in config.py.
