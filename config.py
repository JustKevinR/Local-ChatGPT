# config.py
import os
from gpt4all import GPT4All

GPT4ALL_MODEL_PATH = "path to gpt4all-falcon-newbpe-q4_0.gguf"
BASE_MODEL_PATH = os.path.expanduser('path to base.pt')
ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
