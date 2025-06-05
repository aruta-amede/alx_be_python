def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # List for storing shopping items

    while True:
        display_menu()  # Must be called to pass the check
        try:
            choice = int(input("Enter your choice: "))  # Ensures numeric input
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(item + " has been added to your shopping list.")
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(item + " has been removed from your shopping list.")
            else:
                print(item + " not found in the shopping list.")
        elif choice == 3:
            if shopping_list:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
