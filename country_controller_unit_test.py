import unittest

from mock_db_connection import MockDbConnection
from mock_country_api_connection import MockCountryApiConnection
from country_controller import CountryController
from country import Country

class CountryControllerUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_db_connection = MockDbConnection()
        self.mock_country_api_connection = MockCountryApiConnection()
        self.controller = CountryController(self.mock_db_connection, self.mock_country_api_connection)

    def test_get_countries(self):
        expected_countries = [
            Country("United States", "US"),
            Country("India", "IN"),
            Country("China", "CN")
        ]
        countries = self.controller.get_countries()
        for expected_country, country in zip(expected_countries, countries):
            self.assertEqual(expected_country, country)

    def test_get_country(self):
        code = "US"
        expected_country = Country("United States", "US")
        country = self.controller.get_country(code)
        self.assertEqual(expected_country, country)

    def test_get_sorted_countries(self):
        n = 2
        expected_top_countries = [
            Country("China", "CN"),
            Country("India", "IN")
        ]
        top_countries = self.controller.get_sorted_countries(n)
        for expected_country, country in zip(expected_top_countries, top_countries):
            self.assertEqual(expected_country, country)

if __name__ == "__main__":
    unittest.main()