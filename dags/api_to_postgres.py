
from airflow.decorators import task, dag

from airflow.decorators import gerar_numero_aleatorio, fetch_pokemon_data, add_pokemon_to_db

from datetime import datetime

@dag(dag_id="api_postgres",
     description="pipeline_para_capturar_pokemon",
     start_date=datetime(2025, 10, 5),
     schedule="* * * * *",
     catchup=False)
def api_postgres():

    @task(task_id="gerar_numero_aleatorio")
    def task_gerar_numero_aleatorio():
        return gerar_numero_aleatorio()

    @task(task_id="fetch_pokemon_data")
    def task_fetch_pokemon_data():
        return fetch_pokemon_data()
    
    @task(task_id="add_pokemon_to_db")
    def task_add_pokemon_to_db():
        return add_pokemon_to_db()    
    

    t1 = task_gerar_numero_aleatorio()
    t2 = task_fetch_pokemon_data(t1)
    t3 = task_add_pokemon_to_db(t2)

    t1 >> t2 >> t3 
api_postgres()    