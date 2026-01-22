from fastapi import FastAPI
from app.db.database import engine, Base
from app.routers import ingestion, chat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Palm Mind RAG Backend")
app.include_router(ingestion.router, prefix="/api/v1", tags=["Ingestion"])
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])

@app.get("/")
def home():
    return {"message": "API is running. Go to /docs to test."}