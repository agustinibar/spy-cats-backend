from pydantic import BaseModel
from typing import List, Optional

class TargetCreate(BaseModel):
    name: str
    country: str
    notes: str = ""
    is_complete: bool = False

class MissionCreate(BaseModel):
    targets: List[TargetCreate]

class MissionOut(BaseModel):
    id: int
    is_complete: bool
    cat_id: Optional[int]
    targets: List[TargetCreate]

    class Config:
        from_attributes = True
