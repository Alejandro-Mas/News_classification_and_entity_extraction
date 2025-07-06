import os
import mlflow
import logging
import requests
from collections import Counter

MODEL_ENDPOINT_URL  = os.getenv("MODEL_ENDPOINT_URL") 
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")

def inference_bertopic(news_items: list[dict]) -> list[dict]:
    """
    news_items: lista de dicts con campos 'id' y 'cleaned_text'.
    Devuelve la misma lista con un campo 'topic'.
    """
    documents = [{"id": item["id"], "text": item["cleaned_text"]} for item in news_items]

    try:
        logging.info(f"Iniciando inferencia remota con {len(documents)} textos")

        response = requests.post(
            MODEL_ENDPOINT_URL,
            json={"documents": documents},
            timeout=180
        )
        results = response.json() 
        topics = [item["topic"] for item in results]
        ids = [item["id"] for item in results]
        print(topics)
        logging.info("Inferencia remota completada con éxito")
    except Exception as e:
        logging.exception("Error durante la inferencia remota con BERTopic")
        raise RuntimeError(f"Fallo en la inferencia vía API de BERTopic: {e}") from e


    # Log en MLflow
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment("inference_pipeline")

    with mlflow.start_run(run_name="batch_inference"):
        topic_counts = Counter(topics)
        for topic, count in topic_counts.items():
            mlflow.log_metric(f"topic_{topic}_count", count)
        mlflow.log_param("batch_size", len(news_items))

    return results