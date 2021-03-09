from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from dotenv import load_dotenv
from datetime import datetime, timedelta

ORIGIN_CITY = "BCN"

data_manager = DataManager()
flight_search = FlightSearch()

#Sheety
data_manager.get_destination_data()
data_manager.update_destination_codes()

sheets_data = data_manager.get_destination_data()

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for city in sheets_data:
    destination_code = city['iataCode']
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY,
        destination_city_code=destination_code,
        from_time=today,
        to_time=six_month_from_today)

    if flight is not None:
        print(f"{flight.destination_city} : €{flight.price}")