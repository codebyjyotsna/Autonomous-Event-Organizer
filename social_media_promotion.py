import requests

def post_to_twitter(event_name, event_date, event_location):
    twitter_api_url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": "Bearer YOUR_TWITTER_BEARER_TOKEN"
    }
    payload = {
        "text": f"Join us for {event_name} on {event_date} at {event_location}! Don't miss out! #EventOrganizer"
    }
    response = requests.post(twitter_api_url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Successfully posted to Twitter!")
    else:
        print(f"Failed to post to Twitter: {response.text}")

# Example Usage
if __name__ == "__main__":
    post_to_twitter("AI Club Meetup", "2025-05-15", "Mumbai, India")
