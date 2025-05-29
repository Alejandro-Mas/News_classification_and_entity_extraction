import os
from sqlalchemy import create_engine, text

def get_db_uri():
    user = os.environ.get("MYSQL_USER")
    password = os.environ.get("MYSQL_PASSWORD")
    host = os.environ.get("MYSQL_HOST")
    port = os.environ.get("MYSQL_PORT")
    database = os.environ.get("MYSQL_DATABASE")

    if not all([user, password, host, database]):
        raise ValueError("Faltan variables de entorno para la conexión a la base de datos")

    return f"{host}+pymysql://{user}:{password}@{host}:{port}/{database}"

def get_engine() :
    db_uri = get_db_uri()
    return create_engine(db_uri)

def test_connection():
    try:
        engine = get_engine()
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Conexión exitosa:", result.scalar())
    except Exception as e:
        print("❌ Error al conectar:", e)

if __name__ == "__main__":
    test_connection()