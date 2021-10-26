import requests

endpoint = "https://tequila-api.kiwi.com/v2/search"

headers = {"apikey": "iN2NoEiK7xAqy6gsk1YFmFaPTTnpc9RY"}
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
        url=f"{endpoint}",
        headers=headers,
        params=query,
    )

data = response.json()["data"][0]
# pprint(data)
data_sheet = requests.get(url=endpoint).json()
