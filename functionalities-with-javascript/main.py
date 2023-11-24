import os
import time
from utils import speech_to_text, text_to_speech
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Click button
        # Change colour to red
    # Listen to speech input
        # Change back to green
    return templates.TemplateResponse("test_button_toggle.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def home(request: Request):
    text = speech_to_text()  
    text_to_speech(text)       
    
    return templates.TemplateResponse(
        "test_button_toggle.html", 
        {"request": request, "text": text}
        )