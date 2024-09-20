from country_api_connection import CountryApiConnection

class MockCountryApiConnection(CountryApiConnection):
    def __init__(self, api_url: str="") -> None:
        self.mock_data = [
            {
                "sISOCode":"US",
                "sName":"United States"
            },
            {
                "sISOCode": "IN",
                "sName": "India",
            },
            {
                "sISOCode": "CN",
                "sName": "China"
            }
        ]

    def get_country_info(self) -> dict:
        return self.mock_data