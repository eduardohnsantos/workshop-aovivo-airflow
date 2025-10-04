from time import sleep
from airflow.decorators import dag, task
from airflow.models.baseoperator import chain
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
        return "Primeira atividade iniciada"
    @task
    def segunda_atividade(response):
        print(response)
        sleep(2)
    @task
    def terceira_atividade():
        print("Terceira atividade iniciada")
        sleep(2)
    @task
    def quarta_atividade():
        print("pipeline finalizada")


    t1 = primeira_atividade()
    t2 = segunda_atividade(t1)
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    chain(t1,t2,t3,t4)  

pipeline()