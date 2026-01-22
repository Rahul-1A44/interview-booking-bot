from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.pydantic_models import ChatRequest, ChatResponse
from app.services.rag_service import process_chat_pipeline

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest, db: Session = Depends(get_db)):
    reply, booked = await process_chat_pipeline(request.session_id, request.message, db)
    return ChatResponse(response=str(reply), booking_confirmed=booked)