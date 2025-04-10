from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.Repositories import StreamsRepos as stream_repo
from app.Schemas.StreamSchema import StreamSchema
from app.database import get_db
from typing import List

router = APIRouter()

@router.get("/GetAllStreams", response_model=List[StreamSchema])
async def GetAllStreams(db: AsyncSession = Depends(get_db)):

    db_streams = await stream_repo.GetAllStreams(db)
    return db_streams

@router.get("/GetStreamById/{StreamId}", response_model=StreamSchema)
async def GetStreamById(StreamId: int, db: AsyncSession = Depends(get_db)):

    db_stream = await stream_repo.GetStreamById(db, StreamId)
    if db_stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return db_stream

@router.get("/GetStreamBySourceId/{SourceId}", response_model=List[StreamSchema])
async def GetStreamBySourceId(SourceId: int, db: AsyncSession = Depends(get_db)):

    db_streams = await stream_repo.GetStreamBySourceId(db, SourceId)
    if not db_streams:
        raise HTTPException(status_code=404, detail="Streams not found")
    return db_streams

@router.post("/SaveStream", response_model=StreamSchema)
async def SaveStream(stream: StreamSchema, db: AsyncSession = Depends(get_db)):

    db_stream = await stream_repo.SaveStream(db, stream)
    return db_stream