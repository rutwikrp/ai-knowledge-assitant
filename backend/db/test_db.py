from sqlalchemy import text
from sessions import engine

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT 1")
    )

    print(result.fetchone())