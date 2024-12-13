import json
from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI()

connected_clients: List[WebSocket] = []
messages: List[dict] = []

def save_message_to_file(message: dict):
    with open("messages.txt", "a") as file:
        file.write(json.dumps(message) + "\n")

def load_messages_from_file():
    try:
        with open("messages.txt", "r") as file:
            for line in file:
                messages.append(json.loads(line.strip()))
    except FileNotFoundError:
        pass

@app.on_event("startup")
async def startup_event():
    load_messages_from_file()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    print(f"Client connected: {websocket.client}")

    await websocket.send_text(json.dumps({"type": "message_history", "data": messages}))

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            messages.append(message)
            save_message_to_file(message)

            print(f"Message received: {message}")

            message_to_send = {"type": "new_message", "data": message}

            for client in connected_clients:
                await client.send_text(json.dumps(message_to_send))
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        connected_clients.remove(websocket)
        await websocket.close()
        print(f"Client disconnected: {websocket.client}")
