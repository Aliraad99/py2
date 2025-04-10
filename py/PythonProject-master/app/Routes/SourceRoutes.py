from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.Repositories import SourceRepos as source_repo
from app.Schemas.SourceSchema import SourceSchema
from app.Models.Source import Source
from app.database import get_db
from typing import List

router = APIRouter()

@router.get("/GetAllSources", response_model=List[SourceSchema])
async def GetAllSources(db: AsyncSession = Depends(get_db)):

    db_sources = await source_repo.GetAllSources(db)
    return db_sources
