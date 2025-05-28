def main():
    # Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Validate input
    while priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please enter high, medium, or low.")
        priority = input("Priority (high/medium/low): ").lower()
    
    while time_bound not in ['yes', 'no']:
        print("Please answer with yes or no.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process and display reminder
    print("\n" + generate_reminder(task, priority, time_bound))

def generate_reminder(task, priority, time_bound):
    """Generate a customized reminder message"""
    match priority:
        case "high":
            if time_bound == "yes":
                return f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            else:
                return f"Reminder: '{task}' is a high priority task. Please address it soon."
        case "medium":
            if time_bound == "yes":
                return f"Reminder: '{task}' is a medium priority task that should be completed today."
            else:
                return f"Reminder: '{task}' is a medium priority task. Consider completing it this week."
        case "low":
            if time_bound == "yes":
                return f"Note: '{task}' is a low priority task, but needs to be done today."
            else:
                return f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

if __name__ == "__main__":
    main()