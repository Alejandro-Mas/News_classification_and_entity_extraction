from sqlalchemy import text
from db_utils import get_engine

def test_connection():
    try:
        engine = get_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Conexión exitosa:", result.scalar())
    except Exception as e:
        print("❌ Error al conectar:", e)

if __name__ == "__main__":
    test_connection()