from sqlalchemy import CursorResult

from db_connection import DbConnection

class MockDbConnection(DbConnection):
    def __init__(self) -> None:
        pass

    def execute_query(self, query: str) -> CursorResult:
        return CursorResult()