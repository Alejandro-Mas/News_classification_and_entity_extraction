import logging
from sqlalchemy import text
from db.db_acces import get_engine
from sqlalchemy.exc import SQLAlchemyError

def get_unprocessed_news():
    engine = get_engine()
    try:
        with engine.connect() as conn:

            result = conn.execute(text(get_query()), {"processed": 0})
            news_data = [
                {
                    "id": row.id,
                    "text": f"{row.title or ''} {row.content or ''}"
                }
                for row in result.fetchall()
            ]
            logging.info(f"Recuperadas {len(news_data)} noticias de BD")

            return news_data
    except SQLAlchemyError as e:
        logging.exception('Error recuperando noticias de BD')
        return []

def get_query():
    return """
        SELECT id, title, content 
        FROM news 
        WHERE processed = :processed
    """


if __name__ == "__main__":
    get_unprocessed_news()