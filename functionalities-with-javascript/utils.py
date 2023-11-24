import os
import logging
from pathlib import Path
from playsound import playsound
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_ = load_dotenv(find_dotenv()) # read local .env
openai_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(
    api_key=openai_key
)

def speech_to_text():   
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        logger.info("Say something...")
        audio = r.listen(source)
        
    try:
        text = r.recognize_whisper(audio, language="english")
        logger.info(f"Recognized speech: {text}")
    except sr.UnknownValueError:
        logger.warning("Speech recognition could not understand audio")
    except sr.RequestError as e:
        logger.error("Could not request results from speech recognition API: %s", e)
    
    return text

def text_to_speech(text):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    try:
        response = client.audio.speech.create(
        model="tts-1",
        voice="shimmer",
        input=text
        )
        response.stream_to_file(speech_file_path)
        playsound(speech_file_path)
    except Exception as e:
        logger.error("Error generating speech: %s", e)
    
if __name__ == "__main__":
    text = speech_to_text()
    text_to_speech(text)