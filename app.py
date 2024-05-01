import asyncio
import websockets

async def chat_server(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received message from client: {message}")

start_server = websockets.serve(chat_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
