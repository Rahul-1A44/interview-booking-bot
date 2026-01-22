from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import DocumentMetadata
from app.schemas.pydantic_models import StrategyEnum, IngestionResponse
from app.services import ingestion_service, vector_service

router = APIRouter()

@router.post("/ingest", response_model=IngestionResponse)
async def ingest_document(
    file: UploadFile = File(...),
    strategy: StrategyEnum = Form(...),
    db: Session = Depends(get_db)
):
    content = await file.read()
    text = ingestion_service.extract_text(content)
    chunks = ingestion_service.chunk_text(text, strategy)
    vector_service.store_vectors(chunks, file.filename)
    meta = DocumentMetadata(filename=file.filename, chunking_strategy=strategy)
    db.add(meta)
    db.commit()
    
    return {
        "filename": file.filename,
        "chunks_count": len(chunks),
        "message": "Ingestion and Indexing Complete"
    }