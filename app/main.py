from fastapi import FastAPI, HTTPException, Depends, status
from nats.aio.client import Client as NATS
from uuid import UUID
from .dependencies import get_token_header
from .models import Message
import json

app = FastAPI()
nc = NATS()


@app.post("/publish/{shop_id}")
async def publish_message(shop_id: UUID, message: Message):
    subject = f"updates.{shop_id}"
    message_data = message.dict()
    await nc.publish(subject, json.dumps(message_data).encode('utf-8'))
    return {"status": f"Message sent to shop ID {shop_id}"}


@app.get("/send")
async def send_message():
    # Example of sending a message.
    await nc.publish("updates", b'Item checked out')
    return {"message": "sent"}


@app.on_event("startup")
async def setup_nats():
    # Connect to NATs server / subscribe to a NATs subject
    pass


# handler function for messages
async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")
