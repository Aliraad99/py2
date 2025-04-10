from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.Models.Source import Source
from app.Schemas.SourceSchema import SourceSchema
from sqlalchemy.future import select


async def GetAllSources(db: AsyncSession):
    result = await db.execute(select(Source))
    return result.scalars().all()
    