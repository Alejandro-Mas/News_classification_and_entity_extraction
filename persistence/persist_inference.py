import logging
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db.db_acces import get_engine


def persist_topics(results: list[dict]):
    """
    Actualiza la tabla news con los tópicos inferidos.
    Cada elemento de results debe tener: {'id': int, 'topic': int}
    """
    engine = get_engine()
    try:
        print(get_query())
        with engine.begin() as conn:
        
            for item in results:
                conn.execute(text(get_query()), {"news_id": item["id"], "topic": item["topic"]})

        logging.info(f"Actualizadas {len(results)} noticias con sus tópicos.")
    
    except SQLAlchemyError as e:
        logging.exception("Error al persistir los tópicos en la base de datos.")
        raise RuntimeError(f"Error al actualizar noticias con tópicos: {e}") from e

def get_query():
    return """
        INSERT INTO topics_entities (news_id, topic, persons, organizations, locations)
        VALUES (:news_id, :topic, NULL, NULL, NULL)
        ON DUPLICATE KEY UPDATE
            topic = VALUES(topic)
    """