# In-memory storage for agenda items
agenda = []

def add_agenda_item(start_time, end_time, topic, speaker):
    item = {
        "start_time": start_time,
        "end_time": end_time,
        "topic": topic,
        "speaker": speaker
    }
    agenda.append(item)
    return item

def get_agenda():
    return agenda

# Example Usage
if __name__ == "__main__":
    print("Adding agenda items...")
    add_agenda_item("18:00", "18:30", "Welcome Speech", "John Doe")
    add_agenda_item("18:30", "19:30", "Keynote: The Future of AI", "Jane Smith")

    print("\nEvent Agenda:")
    print(get_agenda())
