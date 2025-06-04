import os
from bertopic import BERTopic
import mlflow
from collections import Counter

MODEL_PATH = os.getenv("BER_TOPIC_MODEL_PATH")

def load_model(model_path=MODEL_PATH):
    return BERTopic.load(model_path)

def predict_topics(model: BERTopic, texts: list[str]) -> list[int]:
    """
    Extrae los tópicos predichos para una lista de textos.
    """
    topics, _ = model.transform(texts)
    return topics

def inference_bertopic(news_items: list[dict], model) -> list[dict]:
    """
    news_items: lista de dicts con campos 'id' y 'cleaned_text'.
    Devuelve la misma lista con un campo 'topic'.
    """
    texts = [item["cleaned_text"] for item in news_items]
    ids = [item["id"] for item in news_items]

    topics, _ = model.transform(texts)

    # Log en MLflow
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("inference_pipeline")

    with mlflow.start_run(run_name="batch_inference"):
        topic_counts = Counter(topics)
        for topic, count in topic_counts.items():
            mlflow.log_metric(f"topic_{topic}_count", count)
        mlflow.log_param("batch_size", len(news_items))

    results = []
    for i in range(len(ids)):
        results.append({
            "id": ids[i],
            "topic": topics[i]
        })
    return results
