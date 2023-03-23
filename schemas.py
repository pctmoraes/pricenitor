from pydantic import BaseModel
from datetime import datetime

class Price(BaseModel):
    store: str
    product: str
    price: float
    date_created: datetime

    class Config:
        orm_mode = True