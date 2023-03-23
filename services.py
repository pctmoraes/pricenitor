from database.models import Price
from database.connection import async_session
from sqlalchemy.future import select

class PriceService:
    async def get_all():
        async with async_session() as session:
            result = await session.execute(select(Price))
            return result.scalars().all()

    async def get_by_id(id: int):
        async with async_session() as session:
            result = await session.execute(select(Price).where(Price.id == id))
            return result.scalar()