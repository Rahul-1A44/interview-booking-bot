from pinecone import Pinecone
from app.core.config import settings
from sentence_transformers import SentenceTransformer

# Load a free, small, and fast model
model = SentenceTransformer('all-MiniLM-L6-v2')

pc = Pinecone(api_key=settings.PINECONE_API_KEY)
index = pc.Index(settings.PINECONE_INDEX_NAME)

def get_embedding(text: str):
    # This runs locally on your CPU (Free)
    return model.encode(text).tolist()

def store_vectors(chunks: list[str], filename: str):
    vectors = []
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        vectors.append({
            "id": f"{filename}_{i}",
            "values": embedding,
            "metadata": {"text": chunk, "source": filename}
        })
    
    # Batch upsert
    index.upsert(vectors=vectors)

def search_vectors(query: str, top_k: int = 3):
    query_emb = get_embedding(query)
    results = index.query(vector=query_emb, top_k=top_k, include_metadata=True)
    return [match['metadata']['text'] for match in results['matches']]