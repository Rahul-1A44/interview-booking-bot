from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.db.database import Base

class DocumentMetadata(Base):
    __tablename__ = "document_metadata"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    upload_date = Column(DateTime, default=datetime.utcnow)
    chunking_strategy = Column(String)

class InterviewBooking(Base):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, index=True)
    candidate_name = Column(String)
    email = Column(String)
    booking_date = Column(String)
    booking_time = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)