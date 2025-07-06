from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from db.data_ingestion.insert_bulk import main

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='nlp_pipeline_ingest_new_docs_using_main',
    default_args=default_args,
    description='Ingest new documents using insert_bulk main function',
    schedule_interval='@daily',  # Ejecutar diariamente
    catchup=False,
    tags=['nlp', 'ingestion'],
) as dag:

    def execute_insert_bulk_main(**kwargs):
        # Ejecuta la función main() desde insert_bulk.py
        main()  # Llama directamente a la función main
        kwargs['ti'].xcom_push(key='ingested', value=True)

    # Tarea que ejecuta el main de insert_bulk
    t1 = PythonOperator(task_id='execute_insert_bulk_main', python_callable=execute_insert_bulk_main)

    # Flujo del DAG
    t1
