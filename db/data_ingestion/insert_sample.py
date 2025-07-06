import os
from sqlalchemy import text
from db.db_acces import get_engine

def insert_sample():
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text("""
            INSERT INTO news (title, content, font, processed)
            VALUES (:title, :content, :font, :processed) """), 
        {
            "title": "Noticia de prueba",
            "content": "Contenido de prueba para validar la inserción.",
            "font": "prueba",
            "processed": 0
        })
        print("Inserción de prueba exitosa.")

if __name__ == "__main__":
    insert_sample()