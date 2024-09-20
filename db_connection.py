from sqlalchemy import Engine, CursorResult, text

class DbConnection():
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def execute_query(self, query: str) -> CursorResult:
        with self.engine.connect() as connection:
            return connection.execute(text(query))