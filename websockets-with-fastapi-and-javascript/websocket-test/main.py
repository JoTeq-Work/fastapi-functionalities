from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import time

from utils import text_to_speech, read_audio_file

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("test_button_toggle.html", {"request": request})

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            transcript = await websocket.receive_text()
            print("Sent to you:", transcript)
            print("Translating to speech")
            text_to_speech(transcript)
            audio_data = read_audio_file("speech")            
            await websocket.send_text(audio_data)
        except WebSocketDisconnect:
            break
    
    await websocket.close()
        
        