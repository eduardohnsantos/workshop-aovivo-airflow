from time import sleep
from airflow.decorators import dag, task
from airflow.models.baseoperator import cross_downstream
from datetime import datetime

@dag(
        dag_id="minha_primeira_dag",
        description="minha etl braba",
        schedule="* * * * *",
        start_date=datetime(2025, 10, 4),
        catchup=False,
)
def pipeline():

    @task
    def primeira_atividade():
        print("Primeira atividade iniciada")
        sleep(2)
    @task
    def segunda_atividade():
        print("Segunda atividade iniciada")
        sleep(2)
    @task
    def terceira_atividade():
        print("Terceira atividade iniciada")
        sleep(2)
    @task
    def quarta_atividade():
        print("pipeline finalizada")


    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

cross_downstream([t1, t2], [t3, t4])    

pipeline()