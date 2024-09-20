from sqlalchemy import CursorResult

from db_connection import DbConnection
from country import Country

class MockDbConnection(DbConnection):
    def __init__(self) -> None:
        pass

    def execute_query(self, query: str) -> CursorResult:
        return CursorResult()

    def insert_countries(self, countries: list[dict]) -> list[dict]:
        return countries
    
    def get_countries(self) -> list[dict]:
        return []

    def get_country(self, code: str) -> dict:
        return Country("United States", "US")
    
    def sort_countries(self) -> list[dict]:
        return []