from fastapi import FastAPI
from nats.aio.client import Client as NATS
from uuid import UUID
from .models import Message
import json
from .api.messaging import router as messaging_router
from datetime import datetime


app = FastAPI()
nc = NATS()
app.include_router(messaging_router)


# Custom encoder function to handle UUID and datetime serialization
def json_encoder(obj):
    if isinstance(obj, (datetime, UUID)):
        return str(obj)
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


@app.post("/publish/{shop_id}")
async def publish_message(shop_id: UUID, message: Message):
    # Serialize the message data to JSON format using custom encoder
    message_json = json.dumps(message.dict(), default=json_encoder).encode('utf-8')
    # Publish the message to the NATs server
    subject = f"updates.store.{shop_id}"
    await nc.publish(subject, message_json)
    return {"status": f"Message sent to shop ID {shop_id}"}


@app.get("/send")
async def send_message():
    # Example of sending a message.
    await nc.publish("updates", b'Item checked out')
    return {"message": "sent"}


'''
Ensure the application can connect to NATS on startup 
and close the connection gracefully on shutdown.
'''


@app.on_event("startup")
async def setup_nats():
    # Connect to the NATS server using the address of the NATS service defined in docker-compose
    await nc.connect("nats://nats-server:4222")


@app.on_event("shutdown")
async def shutdown_nats():
    # Gracefully close the connection to the NATS server
    await nc.drain()


# handler function for messages
async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")
