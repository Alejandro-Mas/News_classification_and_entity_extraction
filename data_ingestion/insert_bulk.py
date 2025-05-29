import os
import pandas as pd
from sqlalchemy import text
from pipeline.db_utils import get_engine

def insert_from_tsv(file_path: str, font_label: str):
    print(f"📄 Procesando: {file_path} con etiqueta '{font_label}'...")

    df = pd.read_csv(file_path, sep="\t")
    df.dropna(subset=["title", "content"], inplace=True)
    df["font"] = font_label
    df["processed"] = 0

    records = df[["title", "content", "font", "processed"]].to_dict(orient="records")

    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO news (title, content, font, processed)
            VALUES (:title, :content, :font, :processed)
        """), records)
        conn.commit()

    print(f"✅ Insertados {len(records)} registros desde {file_path}.")

def main():
    base_path = os.path.join("data_ingestion", "data")
    
    if not os.path.exists(base_path):
        print(f"❌ Carpeta no encontrada: {base_path}")
        return

    for filename in os.listdir(base_path):
        if filename.endswith(".tsv"):
            full_path = os.path.join(base_path, filename)
            font_label = os.path.splitext(filename)[0]  # ej. train.tsv → train
            insert_from_tsv(full_path, font_label)

if __name__ == "__main__":
    main()
