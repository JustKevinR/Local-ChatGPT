# recognizer.py

import speech_recognition as sr
import whisper
import os
from config import BASE_MODEL_PATH

recognizer = sr.Recognizer()
source = sr.Microphone()
base_model = whisper.load_model(BASE_MODEL_PATH)


#listen for command
def listen_for_command():
    with source as s:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        with open("command.wav", "wb") as f:
            f.write(audio.get_wav_data())
        command = base_model.transcribe("command.wav")
        if command and command['text']:
            print("You said:", command['text'])
            return command['text'].lower()
        return None
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None
