from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class StrategyEnum(str, Enum):
    FIXED = "fixed"
    RECURSIVE = "recursive"

class IngestionResponse(BaseModel):
    filename: str
    chunks_count: int
    message: str

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str
    booking_confirmed: bool = False