from country_api_connection import CountryApiConnection

class MockCountryApiConnection(CountryApiConnection):
    def __init__(self, api_url: str="") -> None:
        self.mock_data = {
            "countries": [
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
        }

    def get_country_info(self) -> dict:
        return self.mock_data