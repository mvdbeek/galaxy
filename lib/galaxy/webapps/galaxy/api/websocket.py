import asyncio
import time
from functools import lru_cache
from typing import List

import zmq
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from zmq.asyncio import Context

ctx = Context.instance()
router = APIRouter()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/api/websocket/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.socket = None
        # TODO: check thready safety, should create fastapi dependency

    async def connect(self, websocket: WebSocket):
        if not self.socket:
            self.socket = ctx.socket(zmq.SUB)
            self.socket.bind('tcp://127.0.0.1:5555')
            self.socket.subscribe("")
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get("/")
async def get():
    return HTMLResponse(html)


@lru_cache()
def get_connected_socket():
    # Simulate history events
    ctx = zmq.Context()
    s = ctx.socket(zmq.PUB)
    s.connect('tcp://127.0.0.1:5555')
    time.sleep(1)
    return s


@router.post('/')
async def post(message: str, s=Depends(get_connected_socket)):
    s.send(message.encode())


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):

    async def respond_ws():
        while True:
            msg = await socket.recv()
            data = msg.decode()
            await manager.broadcast(f"Message queue #{client_id} says: {data}")

    async def receive_text():
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")

    await manager.connect(websocket)
    socket = manager.socket
    try:
        while True:
            await asyncio.gather(respond_ws(), receive_text())
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
