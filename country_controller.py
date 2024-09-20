from sqlalchemy import Engine

from country import Country
from db_connection import DbConnection
from country_api_connection import CountryApiConnection

class CountryController():
    def __init__(self, db_connection: DbConnection, api_connection: CountryApiConnection) -> None:
        self.db_connection = db_connection
        self.api_connection = api_connection

    def get_countries(self) -> list[Country]:
        countries = self.db_connection.get_countries()
        if countries:
            return countries
        country_info: list[dict] = self.api_connection.get_country_info()
        for country in country_info:
            countries.append(Country(country["sName"], country["sISOCode"]))
        self.db_connection.insert_countries(countries)
        return countries
    
    def get_country(self, code: str) -> Country:
        country = self.db_connection.get_country(code)
        if country:
            return country
        self.get_countries()
        return self.db_connection.get_country(code)

    def sort_countries(self) -> list[Country]:
        self.get_countries()
        return self.db_connection.sort_countries()
    
    def get_first_n_countries_alphabetically(self, n: int) -> list[Country]:
        countries = self.sort_countries()
        return countries[:n]