import uuid

# In-memory storage for tickets
tickets = []

def create_ticket(attendee_name, attendee_email):
    ticket_id = str(uuid.uuid4())
    ticket = {
        "id": ticket_id,
        "name": attendee_name,
        "email": attendee_email,
    }
    tickets.append(ticket)
    return ticket

def list_tickets():
    return tickets

def find_ticket(ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    return None

# Example Usage
if __name__ == "__main__":
    print("Creating tickets...")
    ticket1 = create_ticket("John Doe", "john@example.com")
    ticket2 = create_ticket("Jane Smith", "jane@example.com")

    print("\nListing all tickets:")
    print(list_tickets())

    print("\nFinding a specific ticket:")
    print(find_ticket(ticket1["id"]))
