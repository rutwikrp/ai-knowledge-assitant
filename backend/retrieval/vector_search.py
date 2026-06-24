from sqlalchemy import text
from db.sessions import engine
from embedding.embedding_service import get_embedding


def search(query: str, top_k: int = 5):

    query_embedding = get_embedding(query)

    vector = str(query_embedding)

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT
                    id,
                    content,
                    embedding <=> CAST(:embedding AS vector) AS distance
                FROM chunks
                ORDER BY distance
                LIMIT :top_k
            """),
            {
                "embedding": vector,
                "top_k": top_k
            }
        )

        return result.fetchall()