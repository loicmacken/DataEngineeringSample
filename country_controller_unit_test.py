import unittest

from mock_db_connection import MockDbConnection
from mock_country_api_connection import MockCountryApiConnection
from country_controller import CountryController

class CountryControllerUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_db_connection = MockDbConnection()
        self.mock_country_api_connection = MockCountryApiConnection()
        self.controller = CountryController(self.mock_db_connection, self.mock_country_api_connection)

    def test_get_country(self):
        code = "US"
        expected_country = {
            "name": "United States",
            "code": "US",
        }
        country = self.controller.get_country(code)
        self.assertEqual(expected_country, country)

    def test_get_countries(self):
        expected_countries = [
            {
                "name": "United States",
                "code": "US",
            },
            {
                "name": "India",
                "code": "IN",
            },
            {
                "name": "China",
                "code": "CN",
            }
        ]
        countries = self.controller.get_countries()
        self.assertEqual(expected_countries, countries)

    def test_sort_countries(self):
        expected_sorted_countries = [
            {
                "name": "China",
                "code": "CN",
            },
            {
                "name": "India",
                "code": "IN",
            },
            {
                "name": "United States",
                "code": "US",
            }
        ]
        sorted_countries = self.controller.sort_countries()
        self.assertEqual(expected_sorted_countries, sorted_countries)

    def test_get_first_n_countries_alphabetically(self):
        n = 2
        expected_top_countries = [
            {
                "name": "China",
                "code": "CN",
            },
            {
                "name": "India",
                "code": "IN",
            }
        ]
        top_countries = self.controller.get_first_n_countries_alphabetically(n)
        self.assertEqual(expected_top_countries, top_countries)

if __name__ == "__main__":
    unittest.main()