import requests
from config import GOOGLE_PLACES_API_KEY

def find_venues(location, attendees):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"event venues in {location}",
        "key": GOOGLE_PLACES_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("results", [])
        # Filter by capacity (dummy filter here)
        return [venue for venue in results if "capacity" not in venue or venue["capacity"] >= attendees]
    else:
        print("Error fetching venues:", response.text)
        return []
