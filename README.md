
# Discord-like Backend with Message Storage

## Description

This project simulates a backend for a messaging application similar to Discord, using **FastAPI**. It includes a WebSocket-based messaging system where messages are stored persistently in a `messages.txt` file. The application provides functionality for real-time communication between clients while ensuring messages are saved and loaded from a file to retain history across sessions.

## Requirements

- Python 3.8 or higher
- FastAPI
- Uvicorn

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ferrerallan/discord-txt-fastapi.git
   ```

2. Navigate to the project directory:
   ```bash
   cd discord-txt-fastapi
   ```

3. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

4. Start the application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

5. The WebSocket endpoint will be available at:
   ```
   ws://127.0.0.1:8000/ws
   ```

## Features

- **WebSocket Communication:** Real-time messaging system using WebSockets.
- **Message Persistence:** Stores messages in `messages.txt` to retain chat history.
- **Message History Broadcast:** On connection, the full message history is sent to the client.
- **Multi-client Support:** Handles multiple simultaneous WebSocket connections.

## Code Overview

### WebSocket Endpoint
The `/ws` endpoint enables WebSocket communication. Clients can:
- Receive the full message history upon connecting.
- Broadcast new messages to all connected clients.

### Message Storage
- **Saving Messages:** Every new message is appended to `messages.txt`.
- **Loading Messages:** On startup, the application loads all messages from `messages.txt` to ensure continuity.

### Key Functions
- `save_message_to_file(message: dict)`: Saves a message to `messages.txt`.
- `load_messages_from_file()`: Loads all messages from `messages.txt` into memory at startup.

### Startup Event
On application startup, `load_messages_from_file` is invoked to load any previously stored messages.

## Example Usage

### Connecting a WebSocket Client
1. Use a WebSocket client (e.g., browser console, Postman, or a dedicated WebSocket client) to connect to the WebSocket endpoint:
   ```javascript
   const ws = new WebSocket("ws://127.0.0.1:8000/ws");
   ws.onmessage = (event) => console.log(JSON.parse(event.data));
   ws.onopen = () => ws.send(JSON.stringify({ user: "Alice", content: "Hello, world!" }));
   ```

2. Once connected:
   - The server sends the full message history.
   - New messages are broadcasted to all connected clients.

## Mode of Use

1. Start the FastAPI server as described above.
2. Connect clients to the WebSocket endpoint.
3. Send and receive real-time messages.
4. Restarting the server retains all previous messages due to the persistence feature.
