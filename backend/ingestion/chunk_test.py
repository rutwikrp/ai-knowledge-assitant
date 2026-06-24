
from backend.ingestion.chunker import chunk_text

chunks = chunk_text(text)

print(len(chunks))