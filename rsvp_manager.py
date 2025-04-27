# In-memory storage for RSVPs
rsvp_list = []

def add_rsvp(name, email, response):
    rsvp = {
        "name": name,
        "email": email,
        "response": response  # 'yes', 'no', or 'maybe'
    }
    rsvp_list.append(rsvp)
    return rsvp

def get_rsvp_list():
    return rsvp_list

# Example Usage
if __name__ == "__main__":
    print("Adding RSVPs...")
    add_rsvp("Alice", "alice@example.com", "yes")
    add_rsvp("Bob", "bob@example.com", "no")

    print("\nRSVP List:")
    print(get_rsvp_list())
