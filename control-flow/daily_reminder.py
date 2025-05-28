def get_valid_input(prompt, valid_options):
    """Helper function to get and validate user input"""
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def generate_reminder(task, priority, time_bound):
    """Generate a perfectly formatted reminder message"""
    time_sensitive_part = "that requires immediate attention today!" if time_bound == "yes" else ""
    
    match priority:
        case "high":
            action = "requires immediate attention" if time_bound == "yes" else "needs your prompt action"
            return f"🚨 Reminder: '{task}' is a HIGH priority task {action}!"
        case "medium":
            urgency = "should be completed today" if time_bound == "yes" else "can be scheduled this week"
            return f"📅 Reminder: '{task}' is a MEDIUM priority task that {urgency}."
        case "low":
            suggestion = "but try to complete it today" if time_bound == "yes" else "for when you have free time"
            return f"💡 Note: '{task}' is a LOW priority task {suggestion}."

def main():
    print("🌟 Daily Task Reminder 🌟")
    print("-------------------------")
    
    # Get validated user input
    task = input("Enter your single most important task today: ").strip()
    priority = get_valid_input("Task priority (high/medium/low): ", ["high", "medium", "low"])
    time_bound = get_valid_input("Is it time-bound? (yes/no): ", ["yes", "no"])
    
    # Generate and display perfect reminder
    reminder = generate_reminder(task, priority, time_bound)
    print("\n" + "="*50)
    print(reminder)
    print("="*50 + "\n")

if __name__ == "__main__":
    main()