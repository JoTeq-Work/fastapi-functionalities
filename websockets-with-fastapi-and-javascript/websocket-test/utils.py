import os
import base64
import logging
from pathlib import Path

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

def text_to_speech(text):
    speech_file_path = "static/audio/speech.mp3"
    try:
        response = client.audio.speech.create(
        model="tts-1",
        voice="shimmer",
        input=text
        )
        response.stream_to_file(speech_file_path)
        # playsound(speech_file_path)
    except Exception as e:
        logger.error("Error generating speech: %s", e)


def read_audio_file(file_name):
    with open(f"static/audio/{file_name}.mp3", "rb") as audio_file:
        audio_data = base64.b64encode(audio_file.read()).decode("utf-8")
    return audio_data

        
if __name__ == "__main__":
    # print("Running function")
    audio_data = read_audio_file("speech")
    print(audio_data)