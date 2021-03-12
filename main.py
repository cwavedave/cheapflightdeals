from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from dotenv import load_dotenv
from datetime import datetime, timedelta
import smtplib
import os

my_email = os.getenv("my_email")
password = os.getenv("password")

email = os.getenv("dest_email")

ORIGIN_CITY = "BCN"

data_manager = DataManager()
flight_search = FlightSearch()

#Sheety
data_manager.get_destination_data()
data_manager.update_destination_codes()

sheets_data = data_manager.get_destination_data()
print(sheets_data)

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
        print(flight.destination_city)
        print(flight.origin_city)
        print(flight.price)
        print(flight.out_date)
        print(flight.return_date)
        print(f"{flight.destination_city} : €{flight.price}")
        if flight.price < city['lowestPrice']:
            print("Cheaper flight found")
            template = f"✈️ New cheap return flight for {flight.origin_city} to {flight.destination_city} found.\nLow price at only €{flight.price}\nCheck {str(flight.out_date)} to {str(flight.return_date)} on https://cwavedave.com/cheap-flights/"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=f"{email}",
                    msg=f"Subject: ✈️ Cheap Flight for {flight.destination_city} \n\n {template}")
