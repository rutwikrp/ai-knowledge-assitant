from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

def get_embedding(text):
    return model.encode(text).tolist()

from embeddings.embedding_service import get_embedding

vec = get_embedding("hello world")

print(len(vec))