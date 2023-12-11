from pydantic import BaseModel, Field, UUID4
from typing import Optional
from datetime import datetime

class Message(BaseModel):
    session_id: UUID4
    shop_id: UUID4
    shopper_id: UUID4
    action_id: int
    create_time: datetime
    action: str
    product_name: str
    product_id: int
    product_price: float
    UPC: str
    category_id: str
    basket_total: float