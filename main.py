from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from dotenv import load_dotenv
from datetime import datetime, timedelta

data_manager = DataManager()

#Sheety
data_manager.get_destination_data()
data_manager.update_destination_codes()

sheets_data = data_manager.get_destination_data()

for city in sheets_data:
    print(city)

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)