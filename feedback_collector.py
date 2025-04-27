# In-memory storage for feedback
feedback_list = []

def collect_feedback(attendee_name, feedback_text):
    feedback = {
        "name": attendee_name,
        "feedback": feedback_text
    }
    feedback_list.append(feedback)
    return feedback

def get_feedback_summary():
    return feedback_list

# Example Usage
if __name__ == "__main__":
    print("Collecting feedback...")
    collect_feedback("Alice", "Great event!")
    collect_feedback("Bob", "Loved the speakers!")

    print("\nFeedback Summary:")
    print(get_feedback_summary())
