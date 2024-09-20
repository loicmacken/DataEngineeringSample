import asyncio

from sqlalchemy import create_engine, text, Engine

MAX_RETRIES = 5

async def main(url: str) -> Engine:
    print("Initializing database...")
    for i in range(MAX_RETRIES):
        try:
            engine = create_engine(url)
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
                return engine
            asyncio.sleep(1)
        else:
            print("Database initialized")
            return engine