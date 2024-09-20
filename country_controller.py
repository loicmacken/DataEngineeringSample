from sqlalchemy import Engine

from country import Country

class CountryController():
    def __init__(self, api_url: str, engine: Engine) -> None:
        self.api_url = api_url
        self.engine = engine

    def get_countries(self) -> list[Country]:
        raise NotImplementedError
    
    def get_country(self, code: str) -> Country:
        raise NotImplementedError

    def sort_countries(self, countries: list[Country]) -> list[Country]:
        raise NotImplementedError
    
    def get_top_countries(self, countries: list[Country], n: int) -> list[Country]:
        raise NotImplementedError