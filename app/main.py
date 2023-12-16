from fastapi import FastAPI, Depends
from nats.aio.client import Client as NATS
from uuid import UUID
from app.nats import nc
from .api.messaging import router as messaging_router
import asyncio


app = FastAPI()

app.include_router(messaging_router)


async def connect_to_nats():
    for _ in range(10):  # Retry connecting for 10 attempts
        try:
            await nc.connect("nats://nats-server:4222")
            print("Connected to NATS")
            return
        except Exception as e:
            print(f"Waiting for NATS: {e}")
            await asyncio.sleep(5)  # Wait for 5 seconds before the next attempt
    print("Failed to connect to NATS after multiple attempts")


'''
Ensure the application can connect to NATS on startup 
and close the connection gracefully on shutdown.
'''


@app.on_event("startup")
async def startup_event():
    await connect_to_nats()



@app.on_event("shutdown")
async def shutdown_nats():
    # Gracefully close the connection to the NATS server
    await nc.drain()


# handler function for messages
async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")
