import requests

endpoint = "https://api.sheety.co/59aae9ada8ccca4f78f6cd14d980ca5b/flightFinder/sheet1"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_info = {}


    def get_destination_data(self):
        data_sheet = requests.get(url=endpoint).json()
        self.destination_info = data_sheet["sheet1"]
        return self.destination_info

    def update_destination_code(self):
        for city in self.destination_info:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            result = requests.put(url=f"{endpoint}/{city['id']}", json=new_data)
            print(result.text)
