from sqlalchemy import Engine

from country import Country
from db_connection import DbConnection
from country_api_connection import CountryApiConnection

class CountryController():
    def __init__(self, db_connection: DbConnection, api_connection: CountryApiConnection) -> None:
        self.db_connection = db_connection
        self.api_connection = api_connection

    def get_countries(self) -> list[Country]:
        raise NotImplementedError
    
    def get_country(self, code: str) -> Country:
        raise NotImplementedError

    def sort_countries(self) -> list[Country]:
        raise NotImplementedError
    
    def get_top_countries(self, n: int) -> list[Country]:
        raise NotImplementedError