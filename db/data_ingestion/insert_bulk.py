import os
import pandas as pd
from sqlalchemy import text
from db.db_acces import get_engine

def insert_from_tsv(file_path: str, font_label: str):
    print(f"Procesando: {file_path} con etiqueta '{font_label}'...")

    # Leer el archivo TSV
    df = pd.read_csv(file_path, sep="\t")
    
    # Eliminar filas con valores nulos en "title" y "content"
    df.dropna(subset=["title", "content"], inplace=True)
    
    # Añadir la etiqueta de la fuente y marcar como procesado
    df["font"] = font_label
    df["processed"] = 1

    # Preparar los registros para la inserción en la tabla 'news'
    news_records = df[["title", "content", "font", "processed"]].to_dict(orient="records")
    
    engine = get_engine()

    with engine.begin() as conn:
        # 1. Insertar registros en la tabla 'news' y capturar los IDs generados
        inserted_ids = []
        for record in news_records:
            result = conn.execute(text("""
                INSERT INTO news (title, content, font, processed)
                VALUES (:title, :content, :font, :processed)
            """), record)
            inserted_id = result.lastrowid
            inserted_ids.append(inserted_id)

        # 2. Preparar los registros para la tabla 'topics_entities'
        entity_records = []
        for i, row in df.iterrows():
            entity_records.append({
                "news_id": inserted_ids[i],
                "topic": int(row["topic"]),  # Aquí es donde tomamos el valor 'topic' del TSV
                "persons": str(row["persons_ner"]),
                "organizations": str(row["organizations_ner"]),
                "locations": str(row["locations_ner"])
            })

        # 3. Insertar múltiples registros en 'topics_entities'
        conn.execute(text("""
            INSERT INTO topics_entities (news_id, topic, persons, organizations, locations)
            VALUES (:news_id, :topic, :persons, :organizations, :locations)
        """), entity_records)

    print(f"Insertados {len(news_records)} registros de noticias y NER desde {file_path}.")

def main():
    base_path = os.path.join("/app","db","data_ingestion")

    if not os.path.exists(base_path):
        print(f"Carpeta no encontrada: {base_path}")
        return

    for filename in os.listdir(base_path):
        if filename.endswith(".tsv"):
            full_path = os.path.join(base_path, filename)
            font_label = "train"
            insert_from_tsv(full_path, font_label)

if __name__ == "__main__":
    main()
