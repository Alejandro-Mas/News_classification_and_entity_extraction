from sqlalchemy import text
from db.db_acces import get_engine


def persist_topics(results: list[dict]):
    """
    Actualiza la tabla `news` con los tópicos inferidos y marca como procesado.
    Cada elemento de `results` debe tener: {'id': int, 'topic': int}
    """
    engine = get_engine()

    with engine.begin() as conn:
        for item in results:
            conn.execute(
                text("""
                    UPDATE news 
                    SET topic = :topic
                    WHERE id = :id
                """),
                {"id": item["id"], "topic": item["topic"]}
            )