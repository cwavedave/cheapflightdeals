import requests
from pprint import pprint
from dotenv import load_dotenv
import os


load_dotenv(".env")

KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
KIWI_QUERY = "locations/query"
KIWI_SEARCH = "v2/search"
SHEETY_ENDPOINT = "https://api.sheety.co/22b8a84df14a589aabfab6a9ff4d57da/cheapFlightsTracker/prices"
API_KEY = os.getenv("API_KEY")


class DataManager:
    def __init__(self):
        self.travel_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        self.travel_data = response.json()['prices']
        # pprint(self.travel_data)
        return self.travel_data

    def update_destination_codes(self):
        print("Active")
        # pprint(self.travel_data)

        for city in self.travel_data:
            #Checks if iataCodes are empty

            if len(city['iataCode']) == 0:
                headers = {
                    "apikey": API_KEY,
                }

                parameters = {
                    "term": city['city']
                }

                #Gets IATA code from City Name through kiwi API
                response = requests.get(url=f"{KIWI_ENDPOINT}/{KIWI_QUERY}",
                                        headers=headers,
                                        params=parameters
                                        )
                response.raise_for_status()
                location = response.json()['locations'][0]['code']

                #Updates the Google Sheets document with IATA Code. Stored as variable - location
                new_data = {
                    "price": {
                        "iataCode": location
                    }
                }
                response = requests.put(
                    url=f"{SHEETY_ENDPOINT}/{city['id']}",
                    json=new_data
                )
                response.raise_for_status()

    def update_prices(self, cheap_city, new_price_record):
        for city in self.travel_data:
            if cheap_city == city['city']:
                new_data = {
                    "price": {
                        "recordCheapest": new_price_record
                    }
                }
                response = requests.put(
                    url=f"{SHEETY_ENDPOINT}/{city['id']}",
                    json=new_data
                )
                response.raise_for_status()