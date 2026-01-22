import json
import google.generativeai as genai
from sqlalchemy.orm import Session
from app.core.config import settings
from app.services.vector_service import search_vectors
from app.db.models import InterviewBooking

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('models/gemini-pro')

MEMORY_DB = {} 

async def process_chat_pipeline(session_id: str, message: str, db: Session):
    if session_id not in MEMORY_DB:
        MEMORY_DB[session_id] = []
    context_list = search_vectors(message)
    context_str = "\n".join(context_list)

    prompt = f"""
    You are a helpful HR assistant for Palm Mind Technology.
    
    CONTEXT FROM UPLOADED DOCUMENTS:
    {context_str}
    
    USER QUERY:
    {message}
    
    INSTRUCTIONS:
    1. Answer the user's question based on the context.
    2. IF the user wants to book an interview, check if they provided Name, Email, Date, and Time.
    3. IF all details are present, output a JSON object ONLY: {{"booking": true, "name": "...", "email": "...", "date": "...", "time": "..."}}.
    4. IF details are missing, ask for them politely.
    5. If it is a normal question, just answer as text.
    """
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
    except Exception as e:
        return f"Error calling Gemini AI: {str(e)}. Please check your API Key in .env", False
    
    final_reply = response_text
    booking_confirmed = False

    if "booking" in response_text and "{" in response_text:
        try:
            clean_json = response_text.replace("```json", "").replace("```", "").strip()
        
            start = clean_json.find("{")
            end = clean_json.rfind("}") + 1
            json_str = clean_json[start:end]
            
            booking_data = json.loads(json_str)
            
            if booking_data.get("booking") == True:
                new_booking = InterviewBooking(
                    candidate_name=booking_data.get("name"),
                    email=booking_data.get("email"),
                    booking_date=booking_data.get("date"),
                    booking_time=booking_data.get("time")
                )
                db.add(new_booking)
                db.commit()
                
                final_reply = f"✅ Booking Confirmed! I have scheduled an interview for {booking_data['name']} on {booking_data['date']}."
                booking_confirmed = True
        except Exception as e:
            print(f"Booking parsing error: {e}")

    # 6. Save History
    MEMORY_DB[session_id].append({"role": "user", "content": message})
    MEMORY_DB[session_id].append({"role": "assistant", "content": final_reply})
    
    return final_reply, booking_confirmed