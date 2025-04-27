import requests

def send_reminder(email, event_name, event_date, event_time):
    email_api_url = "https://api.emailservice.com/send"
    payload = {
        "to": email,
        "subject": f"Reminder: {event_name}",
        "body": f"Hi there! This is a reminder for the {event_name} happening on {event_date} at {event_time}. See you there!",
        "api_key": "YOUR_EMAIL_API_KEY"
    }
    response = requests.post(email_api_url, json=payload)
    if response.status_code == 200:
        print(f"Reminder sent to {email}")
    else:
        print(f"Failed to send reminder to {email}: {response.text}")

# Example Usage
if __name__ == "__main__":
    send_reminder("attendee@example.com", "AI Club Meetup", "2025-05-15", "18:00")
