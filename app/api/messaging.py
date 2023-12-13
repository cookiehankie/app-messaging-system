# app/api/messaging.py
from fastapi import APIRouter, HTTPException
from ..models import Message

router = APIRouter()

@router.post("/messages/", response_model=Message)
async def create_message(message: Message):
    # Logic to publish the message to NATs.io
    return message
