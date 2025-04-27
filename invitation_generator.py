from config import EMAIL_API_KEY
import requests

def generate_invitation(event_details, venue):
    return f"""
    You're invited to the {event_details['name']}!
    When: {event_details['date']} at {event_details['time']}
    Where: {venue['name']}, {venue['formatted_address']}
    """

def send_invitations(event_details, venue):
    invite_text = generate_invitation(event_details, venue)
    email_api_url = "https://api.emailservice.com/send"
    # Dummy email list
    email_list = [f"user{i}@example.com" for i in range(1, 51)]
    for email in email_list:
        payload = {
            "to": email,
            "subject": f"Invitation to {event_details['name']}",
            "body": invite_text,
            "api_key": EMAIL_API_KEY
        }
        response = requests.post(email_api_url, json=payload)
        if response.status_code == 200:
            print(f"Invitation sent to {email}")
        else:
            print(f"Failed to send invitation to {email}: {response.text}")
