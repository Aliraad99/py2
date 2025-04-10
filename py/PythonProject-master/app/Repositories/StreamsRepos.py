from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.Models.Stream import Stream
from app.Schemas.StreamSchema import StreamSchema
from sqlalchemy.future import select


async def GetAllStreams(db: AsyncSession):
    result = await db.execute(select(Stream))
    return result.scalars().all()

async def GetStreamById(db: AsyncSession, StreamId: int):
    result = await db.execute(select(Stream).filter(Stream.id == StreamId))
    return result.scalars().first()

async def GetStreamBySourceId(db: AsyncSession, SourceId: int):
    result = await db.execute(select(Stream).filter(Stream.sourceID == SourceId))
    return result.scalars().all()

async def SaveStream(db: AsyncSession, stream: StreamSchema):
    new_stream = Stream(**stream.dict())
   
   
   
    db.add(new_stream)
    await db.commit()
    await db.refresh(new_stream)
    return new_stream

