from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# DAG de exemplo
with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2025, 10, 4),
    schedule="* * * * *",   # ⏱️ Executa a cada 1 minuto
    catchup=False,
    tags=["example"],
) as dag:

    start = EmptyOperator(task_id="start")
    hello = EmptyOperator(task_id="hello")
    end = EmptyOperator(task_id="end")

    # Definindo dependências
    start >> hello >> end
