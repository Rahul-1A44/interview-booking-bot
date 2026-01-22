# Palm Mind Backend Assignment

## 📋 Overview
This is a modular **FastAPI** backend designed for **Document Ingestion** and **Conversational RAG (Retrieval-Augmented Generation)**. It was built as a technical task for the Backend Developer position at Palm Mind Technology.

The system allows users to upload PDF documents, index them using vector embeddings, and perform intelligent queries—including an AI-driven **Interview Booking System**.

## 🛠 Tech Stack
- **Framework:** FastAPI (Python 3.12)
- **LLM:** Google Gemini 1.5 Flash (Optimized for speed and free-tier access)
- **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`) running locally for cost-efficiency.
- **Vector Database:** Pinecone (Serverless)
- **Database:** SQLite (managed via SQLAlchemy)
- **Architecture:** Service-based modular pattern.

## 🚀 Features
1. **Document Ingestion API:**
   - Uploads `.pdf` files.
   - Extracts text and chunks it using a fixed-size strategy.
   - Generates vector embeddings locally.
   - Stores vectors in Pinecone and metadata in SQLite.

2. **Conversational RAG API:**
   - Retrieves relevant context from uploaded documents.
   - Uses **Google Gemini** to generate natural answers.
   - **Smart Booking Logic:** Detects if a user wants to book an interview, extracts details (Name, Email, Date, Time), and saves the booking to the SQL database.

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/Rahul-1A44/interview-booking-bot](https://github.com/Rahul-1A44/interview-booking-bot)
cd interview-booking-bot
2. Create Virtual Environment
Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your keys:

Ini, TOML

# Pinecone Configuration
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=rag-index

# Google Gemini Configuration
GEMINI_API_KEY=your_google_gemini_key

# Database Configuration
DATABASE_URL=sqlite:///./interview_task.db
REDIS_URL=redis://localhost:6379/0
5. Run the Server
Bash

uvicorn app.main:app --reload
The API will be available at: http://127.0.0.1:8000/docs

🧪 How to Test
1. Ingest a Document
Go to POST /api/v1/ingest

Upload a sample PDF (e.g., a resume).

Execute.

2. Chat & Booking
Go to POST /api/v1/chat

Ask a question: {"session_id": "test", "message": "What is this document about?"}

Book an interview: {"session_id": "test", "message": "I want to book an interview"}

Provide details: {"session_id": "test", "message": "Name is Rahul, email rahul@test.com, date 2026-05-20, time 10 AM"}

Result: The system will confirm the booking and save it to the database.

🧠 Architectural Decisions
Why Local Embeddings?
To ensure the project is cost-efficient and easy to run on any machine without requiring paid OpenAI credits, I utilized sentence-transformers. This provides high-quality embeddings running entirely on the CPU.

Why Google Gemini?
I selected Google Gemini (1.5 Flash) for the LLM component because it offers excellent reasoning capabilities for entity extraction (booking details) and provides a robust free tier for development.

In-Memory Memory Manager
While the architecture supports Redis, I implemented an In-Memory Adapter for chat history. This ensures the project runs immediately after cloning without requiring the reviewer to install and configure a local Redis server.

🔮 Future Improvements
If I had more time, I would love to add:

User Authentication: Add JWT based login so only authorized users can book interviews.

Dockerization: Create a Dockerfile and docker-compose to make deployment even easier.

Advanced Parsing: Add OCR support for scanned PDF documents.

👤 Author
Rahul Kumar Gupta Submitted for Palm Mind Technology


### **Step 2: Commit and Push (The "Active Developer" Look)**
Now, run these commands to push this update. This creates a timestamped "work history" on GitHub.

