import requests
from config import ZOMATO_API_KEY

def find_catering_options(location, attendees):
    url = "https://developers.zomato.com/api/v2.1/search"
    headers = {
        "user-key": ZOMATO_API_KEY
    }
    params = {
        "q": "catering",
        "count": 10,
        "entity_type": "city",
        "entity_id": location
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        results = response.json().get("restaurants", [])
        return [catering["restaurant"]["name"] for catering in results]
    else:
        print("Error fetching catering options:", response.text)
        return []
