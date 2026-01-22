import fitz  # PyMuPDF
from app.schemas.pydantic_models import StrategyEnum

def extract_text(file_bytes: bytes) -> str:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text: str, strategy: StrategyEnum) -> list[str]:
    if strategy == StrategyEnum.FIXED:
        # Fixed size: 500 chars with 50 overlap
        chunk_size = 500
        overlap = 50
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size-overlap)]
    
    elif strategy == StrategyEnum.RECURSIVE:
        # Split by double newlines (paragraphs), then single newlines
        import re
        chunks = re.split(r'\n\s*\n', text)
        return [c.strip() for c in chunks if c.strip()]
    
    return [text]