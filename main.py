import time

from sqlalchemy import create_engine, text, Engine

url = "postgresql+psycopg2://postgres:postgres@db:5432/DB"

MAX_RETRIES = 5

print("Initializing database...")
for i in range(MAX_RETRIES):
    try:
        engine: Engine = create_engine(url)
        with engine.connect() as connection:
            with open("init.sql") as query_file:
                query = query_file.read()
                connection.execute(
                    text(query)
                )
    except Exception as e:
        print(f"Error: {e}")
        if i < MAX_RETRIES - 1:
            print("Retrying...")
        else:
            print("Max retries reached")
            break
        time.sleep(5)
    else:
        print("Database initialized")
        break