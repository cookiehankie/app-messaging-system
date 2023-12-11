from fastapi import FastAPI
import asyncio
from nats.aio.client import Client as NATS

app = FastAPI()
nc = NATS()

@app.on_event("startup")
async def setup_nats():
    # Connect to NATs server.
    await nc.connect("nats://localhost:4222")

@app.get("/send")
async def send_message():
    # Example of sending a message.
    await nc.publish("updates", b'Item checked out')
    return {"message": "sent"}


