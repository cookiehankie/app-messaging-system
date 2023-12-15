# app/api/messaging.py
# a Pydantic model Message in models.py that will validate the data being sent to the endpoint.

from fastapi import APIRouter
from app.models import Message

router = APIRouter()

@router.post("/messages/", response_model=Message)
async def create_message(message: Message):
    # Logic to publish the message to NATs.io
    return message
