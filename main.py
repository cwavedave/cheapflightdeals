from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from dotenv import load_dotenv

data_manager = DataManager()

#Sheety
data_manager.get_destination_data()
data_manager.update_destination_codes()

sheets_data = data_manager.get_destination_data()

for city in sheets_data:
    print(city)

# # FLIGHT SEARCH API
# # Search one-way and return via Booking tool or implement your own integration.
# FLIGHTS_API = "mglJ_d0MTyu4zMEiWMDYh7BZU75bcCm0"
# FLIGHTS_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
#
# header = {
#     "apikey" : FLIGHTS_API,
# }
#
# parameters = {
#      "fly_from": "BCN",
#      "fly_to": "LON",
#      "date_from": "01/03/2021",
#      "date_to" : "14/03/2021",
# }
#
# response = requests.get(url=FLIGHTS_ENDPOINT, params = parameters, headers=header)
# print(response.json())