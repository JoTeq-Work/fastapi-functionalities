import os
import pyttsx3
from pathlib import Path
from openai import OpenAI
from playsound import playsound
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env
openai_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input="NanoMatriX confirms that your space has been created"
)
response.stream_to_file(speech_file_path)
playsound(speech_file_path)



"""Pyttsx (Python text to speech)"""
# engine = pyttsx3.init()

# # Change voice
# voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[0].id) # 0 - male voice
# engine.setProperty('voice', voices[1].id) # 1 - female voice
# engine.say("Hi there, how are you?")
# engine.runAndWait()