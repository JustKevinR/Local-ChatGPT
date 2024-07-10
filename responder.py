# recognizer.py
import sys
from os import system
from config import ALLOWED_CHARS

if sys.platform != 'darwin':
    import pyttsx3
    engine = pyttsx3.init()

def respond(text):
    if sys.platform == 'darwin':
        clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)
        system(f"say '{clean_text}'")
    else:
        engine.say(text)
        engine.runAndWait()
