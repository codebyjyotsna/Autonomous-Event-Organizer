from venue_finder import find_venues
from invitation_generator import send_invitations
from catering_manager import find_catering_options
from ticketing_system import create_ticket, list_tickets
from rsvp_manager import add_rsvp, get_rsvp_list
from social_media_promotion import post_to_twitter
from feedback_collector import collect_feedback, get_feedback_summary
from agenda_manager import add_agenda_item, get_agenda
from reminder_notifications import send_reminder

def main():
    # Event Details
    event_details = {
        "name": "AI Club Meetup",
        "location": "Mumbai",
        "date": "2025-05-15",
        "time": "18:00",
        "attendees": 50
    }

    # Step 1: Find Venues
    print("Step 1: Finding venues...")
    venues = find_venues(event_details["location"], event_details["attendees"])
    if venues:
        selected_venue = venues[0]  # Select the first venue for simplicity
        print(f"Selected Venue: {selected_venue['name']}, {selected_venue['formatted_address']}")
    else:
        print("No venues found. Exiting...")
        return

    # Step 2: Generate and Send Invitations
    print("Step 2: Generating and sending invitations...")
    send_invitations(event_details, selected_venue)

    # Step 3: Find Catering Options
    print("Step 3: Finding catering options...")
    catering_options = find_catering_options(event_details["location"], event_details["attendees"])
    if catering_options:
        print(f"Available Catering Options: {', '.join(catering_options)}")
    else:
        print("No catering options found.")

    # Step 4: Ticketing System
    print("Step 4: Creating tickets...")
    for i in range(event_details["attendees"]):
        create_ticket(f"Attendee {i+1}", f"attendee{i+1}@example.com")
    print(f"Tickets Created: {len(list_tickets())}")

    # Step 5: RSVP Management
    print("Step 5: Adding RSVPs...")
    add_rsvp("Alice", "alice@example.com", "yes")
    add_rsvp("Bob", "bob@example.com", "no")
    print(f"RSVP List: {get_rsvp_list()}")

    # Step 6: Social Media Promotion
    print("Step 6: Promoting event on social media...")
    post_to_twitter(event_details["name"], event_details["date"], event_details["location"])

    # Step 7: Agenda Management
    print("Step 7: Creating event agenda...")
    add_agenda_item("18:00", "18:30", "Welcome Speech", "John Doe")
    add_agenda_item("18:30", "19:30", "Keynote: The Future of AI", "Jane Smith")
    print(f"Event Agenda: {get_agenda()}")

    # Step 8: Reminder Notifications
    print("Step 8: Sending reminders to attendees...")
    for ticket in list_tickets():
        send_reminder(ticket["email"], event_details["name"], event_details["date"], event_details["time"])

    # Step 9: Collect Feedback
    print("Step 9: Collecting feedback...")
    collect_feedback("Alice", "Great event!")
    collect_feedback("Bob", "Loved the speakers!")
    print(f"Feedback Summary: {get_feedback_summary()}")

    print("Event organization completed successfully!")

if __name__ == "__main__":
    main()
