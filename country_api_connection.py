import requests

class CountryApiConnection:
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def get_country_info(self) -> dict:
        response = requests.get(self.api_url)
        return response.json()