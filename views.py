from fastapi import APIRouter, HTTPException
from services import PriceService
from schemas import Price
from typing import List

price = APIRouter(prefix='/price')

@price.get('/all', response_model=List[Price])
async def get_all():
    try:
        return await PriceService.get_all()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@price.get('/{id}', response_model=Price)
async def get_by_id(id: int):
    try:
        result = await PriceService.get_by_id(id)
        return result
    except Exception as error:
        raise HTTPException(400, detail=str(error))