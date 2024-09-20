import time
import os

from sqlalchemy import create_engine, Engine

from db_connection import DbConnection
from country_controller import CountryController
from country_api_connection import CountryApiConnection

db_url = "postgresql+psycopg2://postgres:postgres@db:5432/DB"
api_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso/ListOfCountryNamesByCode/JSON/debug?"

MAX_RETRIES = 5
ENV = "prod"
N_COUNTRIES = os.getenv("N_COUNTRIES", 5)

print("Initializing database...")
for i in range(MAX_RETRIES):
    try:
        engine: Engine = create_engine(db_url)
        connection = DbConnection(engine)
        with open("init.sql") as query_file:
            query = query_file.read()
            connection.execute_query(query)
    except Exception as e:
        print(f"Error: {e}")
        if i < MAX_RETRIES - 1:
            print("Retrying...")
        else:
            print("Max retries reached")
            exit(1)
        time.sleep(5)
    else:
        print("Database initialized")
        break

if ENV == "test":
    import unittest
    from country_controller_unit_test import CountryControllerUnitTest
    test_suite = unittest.TestLoader().loadTestsFromTestCase(CountryControllerUnitTest)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
else:
    api_connection = CountryApiConnection(api_url)
    controller = CountryController(connection, api_connection)

    print(f"Getting {N_COUNTRIES} countries...")
    countries = controller.get_first_n_countries_alphabetically(N_COUNTRIES)
    print("Countries:")
    for country in countries:
        print(country)
    print("Done")