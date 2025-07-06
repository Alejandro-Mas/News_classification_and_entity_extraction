import logging
from sqlalchemy import text
from db.db_acces import get_engine
from sqlalchemy.exc import SQLAlchemyError

def persist_ner_results(enriched_data: list[dict]):
    """
    Inserta o actualiza los resultados enriquecidos (topic + entidades NER)
    en la tabla topic_entities.
    """
    engine = get_engine()
    try:
        with engine.begin() as conn:
            for item in enriched_data:
                conn.execute(
                    text(get_update_topic_entities()),
                    {
                        "id": item["id"],
                        "persons": ", ".join(item.get("persons", [])),
                        "organizations": ", ".join(item.get("organizations", [])),
                        "locations": ", ".join(item.get("locations", [])),
                    }
                )

            # Marcamos como procesado
            for item in enriched_data:
                conn.execute(
                    text(get_update_news()), {"id": item["id"], "processed": 1}
                )
            logging.info(f"Persistidos {len(enriched_data)} documentos en topic_entities y marcados como procesados.")
    except SQLAlchemyError as e:
        logging.exception("Error al persistir resultados de NER en la base de datos.")
        raise RuntimeError(f"Fallo al actualizar entidades NER en BD: {e}") from e

def get_update_topic_entities():
    return """
        UPDATE topics_entities
        SET
            persons = :persons,
            organizations = :organizations,
            locations = :locations
        WHERE news_id = :id
    """
    
def get_update_news():
    return """
        UPDATE news 
        SET processed = :processed 
        WHERE id = :id
    """
