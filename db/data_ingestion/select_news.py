import os
from sqlalchemy import text
from db.db_acces import get_engine

def get_unprocessed_news():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT * FROM news WHERE processed = :processed
        """), {"processed": 0})

        news_items = result.fetchall()

        news_data = [
            {
                "id": row.id,
                "text": f"{row.title or ''} {row.content or ''}",  # concatenamos
                "font": row.font
            }
            for row in news_items
        ]

        return news_data

if __name__ == "__main__":
    select_unprocessed_news()