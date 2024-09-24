from sqlalchemy import Engine

from country import Country
from db_connection import DbConnection
from country_api_connection import CountryApiConnection

class CountryController():
    def __init__(self, db_connection: DbConnection, api_connection: CountryApiConnection) -> None:
        self.db_connection = db_connection
        self.api_connection = api_connection

    def get_countries(self) -> list[Country]:
        country_info: list[dict] = self.api_connection.get_country_info()
        countries = []
        for country in country_info:
            countries.append(Country(country["sName"], country["sISOCode"]))
        self.db_connection.insert_countries(countries)
        return countries
    
    def get_country(self, code: str) -> Country:
        return self.db_connection.get_country(code)

    def get_sorted_countries(self, n_countries: int = -1) -> list[Country]:
        countries = self.get_countries()
        countries.sort(key=lambda country: country.name)
        if n_countries == -1:
            return countries
        return countries[:n_countries]