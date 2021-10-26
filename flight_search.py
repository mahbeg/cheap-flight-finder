import requests
from _datetime import datetime, timedelta
from flight_data import FlightData

location_endpoint = "https://tequila-api.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.header = {"apikey": "iN2NoEiK7xAqy6gsk1YFmFaPTTnpc9RY"}
        self.date_from = datetime.now().date() + timedelta(days=1)
        self.date_to = datetime.now() + timedelta(days=(30*6))
        self.city = "Berlin"
        self.parameters = {}

    def get_destination_code(self, city_name):
        parameters = {"term": city_name, "location_types": "city"}
        header = {"apikey": "iN2NoEiK7xAqy6gsk1YFmFaPTTnpc9RY"}
        result = requests.get(url=f"{location_endpoint}/locations/query", params=parameters, headers= header).json()
        location_result = result["locations"]
        code = location_result[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = self.header
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{location_endpoint}",
            headers=headers,
            params=query,
        )

        data = response.json()["data"][0]
        # pprint(data)

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data




