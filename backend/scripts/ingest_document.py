import os

from sqlalchemy import text

from db.sessions import engine
from ingestion.pdf_loader import extract_pdf_text
from ingestion.chunker import chunk_text
from embedding.embedding_service import get_embedding


def ingest_pdf(pdf_path):

    filename = os.path.basename(pdf_path)

    text_content = extract_pdf_text(pdf_path)

    chunks = chunk_text(text_content)

    with engine.begin() as conn:

        document_id = conn.execute(
            text("""
                INSERT INTO documents
                (
                    title,
                    source,
                    team,
                    version
                )

                VALUES
                (
                    :title,
                    'local',
                    'devops',
                    '1.0'
                )

                RETURNING id
            """),
            {
                "title": filename
            }
        ).scalar()

        for index, chunk in enumerate(chunks):

            embedding = get_embedding(chunk)

            conn.execute(
                text("""
                    INSERT INTO chunks
                    (
                        document_id,
                        chunk_index,
                        content,
                        embedding
                    )

                    VALUES
                    (
                        :document_id,
                        :chunk_index,
                        :content,
                        :embedding
                    )
                """),
                {
                    "document_id": document_id,
                    "chunk_index": index,
                    "content": chunk,
                    "embedding": str(embedding)
                }
            )

    print(
        f"Stored {len(chunks)} chunks from {filename}"
    )


if __name__ == "__main__":

    ingest_pdf("TheTerraformBook_sample.pdf")