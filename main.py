from fastapi import FastAPI, Depends, HTTPException
import asyncio
from uuid import UUID
from nats.aio.client import Client as NATS
from dependencies import get_token_header
from models import Message

app = FastAPI()
nc = NATS()

# Publish Endpoint
@app.post("/publish/{shop_id}")
async def publish_message(shop_id: UUID, message: Message, token: str = Depends(get_token_header)):
    subject = f"updates.{shop_id}"
    message_json = message.json().encode('utf-8')
    # Here you would publish to NATs
    return {"status": f"Message sent to shop ID {shop_id}"}


@app.on_event("startup")
async def setup_nats():
    # Connect to NATs server / subscribe to a NATs subject
    pass

# handler function for messages
async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")


@app.get("/send")
async def send_message():
    # Example of sending a message.
    await nc.publish("updates", b'Item checked out')
    return {"message": "sent"}


