import spacy
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

from db.db_acces import get_engine

from db.data_ingestion.select_news import get_unprocessed_news

from preprocessing.clean_text import clean_news_items

from modeling.bertopic.inference_bertopic import inference_bertopic, load_model
from persistence.persist_inference import persist_topics

from modeling.ner.ner_extraction import extract_entities_batch
from persistence.ner_persistence import persist_ner_results


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='nlp_pipeline_dag',
    default_args=default_args,
    description='NLP pipeline with topic modeling and NER',
    schedule_interval='@daily',
    catchup=False,
    tags=['nlp', 'pipeline'],
) as dag:

    def fetch_news(**kwargs):
        news = get_unprocessed_news()
        if not news:
            print("No hay noticias nuevas.")
        kwargs['ti'].xcom_push(key='raw_news', value=news)

    def clean_text(**kwargs):
        raw_news = kwargs['ti'].xcom_pull(task_ids='fetch_news', key='raw_news')
        cleaned = clean_news_items(raw_news)
        kwargs['ti'].xcom_push(key='cleaned_news', value=cleaned)

    def run_inference(**kwargs):
        cleaned_news = kwargs['ti'].xcom_pull(task_ids='clean_text', key='cleaned_news')
        model = load_model()  # ✅ cargado una sola vez por batch, (ampliacion -> dejar el modelo levantado en un endpoint para inferencia)
        results = inference_bertopic(cleaned_news, model)
        kwargs['ti'].xcom_push(key='topic_results', value=results)

    def persist_results(**kwargs):
        results = kwargs['ti'].xcom_pull(task_ids='inference_bertopic', key='topic_results')
        persist_topics(results)

    def extract_ner(**kwargs):
        cleaned_news = kwargs['ti'].xcom_pull(task_ids='clean_text', key='cleaned_news')
        nlp_model = spacy.load("en_core_web_sm")  # ✅ cargado una vez
        ner_results = extract_entities_batch(cleaned_news, nlp_model)
        kwargs['ti'].xcom_push(key='ner_results', value=ner_results)

    def persist_ner(**kwargs):
        ner_data = kwargs['ti'].xcom_pull(task_ids='extract_ner', key='ner_results')
        persist_ner_results(ner_data)

    # Tasks
    t1 = PythonOperator(task_id='fetch_news', 			python_callable=fetch_news)
    t2 = PythonOperator(task_id='clean_text', 			python_callable=clean_text)
    t3 = PythonOperator(task_id='inference_bertopic', 	python_callable=run_inference)
    t4 = PythonOperator(task_id='persist_results', 		python_callable=persist_results)
    t5 = PythonOperator(task_id='extract_ner', 			python_callable=extract_ner)
    t6 = PythonOperator(task_id='persist_ner', 			python_callable=persist_ner)

    # Flujo del DAG
    t1 >> t2 >> t3 >> t4 >> t5 >> t6
