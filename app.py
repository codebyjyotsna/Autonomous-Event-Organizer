from venue_finder import find_venues
from invitation_generator import send_invitations
from catering_manager import find_catering_options

def main():
    # Input details
    event_details = {
        "name": "AI Club Meetup",
        "location": "Mumbai",
        "date": "2025-05-15",
        "time": "18:00",
        "attendees": 50
    }

    print("Step 1: Finding venues...")
    venues = find_venues(event_details["location"], event_details["attendees"])
    print(f"Found {len(venues)} venue options.")

    print("Step 2: Generating and sending invitations...")
    send_invitations(event_details, venues[0])  # Select the first venue for simplicity

    print("Step 3: Finding catering options...")
    catering_options = find_catering_options(event_details["location"], event_details["attendees"])
    print(f"Found {len(catering_options)} catering options.")

    print("Event organization completed!")

if __name__ == "__main__":
    main()
