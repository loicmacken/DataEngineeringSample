from sqlalchemy import Engine, CursorResult, text

from country import Country

class DbConnection():
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def execute_query(self, query: str) -> CursorResult:
        with self.engine.connect() as connection:
            return connection.execute(text(query))

    def insert_countries(self, countries: list[Country]) -> list[Country]:
        query = "INSERT INTO countries (name, code) VALUES "
        for country in countries:
            country.name = country.name.replace("'", "''")
            query += f"('{country.name}', '{country.code}'), "
        query = query[:-2] + ";"
        self.execute_query(query)
        return countries
    
    def get_countries(self) -> list[Country]:
        query = "SELECT * FROM countries;"
        result = self.execute_query(query)
        countries = []
        for row in result:
            countries.append(Country(row["name"], row["code"]))
        return countries
    
    def get_country(self, code: str) -> Country:
        query = f"SELECT * FROM countries WHERE code = '{code}';"
        result = self.execute_query(query)
        row = result.fetchone()
        return Country(row["name"], row["code"])
    
    def sort_countries(self) -> list[Country]:
        query = "SELECT * FROM countries ORDER BY name;"
        result = self.execute_query(query)
        countries = []
        for row in result:
            countries.append(Country(row["name"], row["code"]))
        return countries