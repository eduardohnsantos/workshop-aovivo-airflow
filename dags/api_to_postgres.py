from airflow.decorators import task, dag
from datetime import datetime
import requests, random, psycopg2

@dag(
    dag_id="api_postgres",
    description="pipeline_para_capturar_pokemon",
    start_date=datetime(2025, 10, 5),
    schedule="* * * * *",
    catchup=False
)
def api_postgres():

    @task(task_id="gerar_numero_aleatorio")
    def gerar_numero_aleatorio():
        return random.randint(1, 151)

    @task(task_id="fetch_pokemon_data")
    def fetch_pokemon_data(pokemon_id: int):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url)
        return response.json()

    @task(task_id="add_pokemon_to_db")
    def add_pokemon_to_db(pokemon_data: dict):
        conn = psycopg2.connect(
            host="seu_host",
            dbname="seu_db",
            user="seu_usuario",
            password="sua_senha"
        )
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO pokemons (id, name, base_experience) VALUES (%s, %s, %s)",
            (pokemon_data["id"], pokemon_data["name"], pokemon_data["base_experience"])
        )
        conn.commit()
        cur.close()
        conn.close()
        return f"Pokemon {pokemon_data['name']} inserido com sucesso!"

    @task(task_id="print_de_sucesso")
    def print_de_sucesso(response):
        print(response)

    # Definindo o fluxo
    pokemon_id = gerar_numero_aleatorio()
    pokemon_data = fetch_pokemon_data(pokemon_id)
    insert_response = add_pokemon_to_db(pokemon_data)
    print_de_sucesso(insert_response)


api_postgres()
