from pydantic import BaseModel
from fastapi import Body
 


class SourceSchema(BaseModel):
            id : int
            source_name : str
            source_url : str

            class Config:
                from_attributes = True






