# app/api/messaging.py
# a Pydantic model Message in models.py that will validate the data being sent to the endpoint.

from fastapi import APIRouter, Depends
from app.models import Message
from app.nats import nc
from nats.aio.client import Client as NATS
from datetime import datetime
from uuid import UUID
from ..models import Message
import json


router = APIRouter()


# Custom encoder function to handle UUID serialization
def json_encoder(obj):
    if isinstance(obj, (datetime, UUID)):
        return str(obj)
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


@router.get("/send")
async def send_message():

    # Example of sending a message.
    await nc.publish("updates", b'Item')
    return {"message": "sent"}


@router.post("/publish/{shop_id}")
async def publish_message(shop_id: UUID, message: Message):
    # Serialize the message data to JSON format using custom encoder
    message_json = json.dumps(message.dict(), default=json_encoder).encode('utf-8')
    # Publish the message to the NATs server
    subject = f"updates.store.{shop_id}"
    print(subject)
    await nc.publish(subject, message_json)
    return {"status": f"Message sent to shop ID {shop_id}"}


