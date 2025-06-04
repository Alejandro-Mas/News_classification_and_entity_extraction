from sqlalchemy import text
from db.db_acces import get_engine

def persist_ner_results(enriched_data: list[dict]):
    """
    Inserta o actualiza los resultados enriquecidos (topic + entidades NER)
    en la tabla `news_enriched`.
    """
    engine = get_engine()
    with engine.begin() as conn:
        for item in enriched_data:
            conn.execute(
                text("""
                    INSERT INTO news_enriched (news_id, topic, persons, organizations, locations)
                    VALUES (:id, :topic, :persons, :organizations, :locations)
                    ON DUPLICATE KEY UPDATE
                        topic = VALUES(topic),
                        persons = VALUES(persons),
                        organizations = VALUES(organizations),
                        locations = VALUES(locations)
                """),
                {
                    "id": item["id"],
                    "topic": item.get("topic"),
                    "persons": ", ".join(item.get("persons", [])),
                    "organizations": ", ".join(item.get("organizations", [])),
                    "locations": ", ".join(item.get("locations", [])),
                }
            )

        # Marcamos como procesado
        for item in enriched_data:
            conn.execute(
                text("UPDATE news SET processed = 1 WHERE id = :id"),
                {"id": item["id"]}
            )
