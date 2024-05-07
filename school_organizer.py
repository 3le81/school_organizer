import csv
import os
from tabulate import tabulate
from datetime import datetime

# Constants
EVENTS_FOLDER = 'events'


# Function to clear the screen once the program runs
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to load events for a child
def load_events(child_name):
    events = []
    file_path = os.path.join(EVENTS_FOLDER, f"{child_name}.csv")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                events.append(row)
    return events


# Function to save events for a child
def save_events(child_name, events):
    file_path = os.path.join(EVENTS_FOLDER, f"{child_name}.csv")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(events)


# Function to add a child
def add_child(child_name):
    file_path = os.path.join(EVENTS_FOLDER, f"{child_name}.csv")
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            pass
        print(f"Child '{child_name}' added successfully.")
    else:
        print(f"Child '{child_name}' already exists.")


# Function to remove a child
def remove_child(child_name):
    file_path = os.path.join(EVENTS_FOLDER, f"{child_name}.csv")
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Child '{child_name}' removed successfully.")
    else:
        print(f"Child '{child_name}' does not exist.")


# Function to select a child
def select_child():
    child_name = input("Enter child's name: ")
    file_path = os.path.join(EVENTS_FOLDER, f"{child_name}.csv")
    if os.path.exists(file_path):
        return child_name
    else:
        print(f"Child '{child_name}' does not exist.")
        return None


# Function to add an event for a child
def add_event(child_name, event, day, month, year):
    date = f"{day}-{month}-{year}"
    events = load_events(child_name)
    events.append([date, event])
    save_events(child_name, events)
    print("Event added successfully.")


# Function to view events for a child
def view_events(child_name):
    events = load_events(child_name)
    if events:
        headers = ["Index", "Date", "Event"]
        table_data = [(idx, event[0], event[1])
                      for idx, event in enumerate(events, 1)]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("No events available.")


# Function to delete an event for a child
def delete_event(child_name, event_index):
    events = load_events(child_name)
    if 1 <= event_index <= len(events):
        del events[event_index - 1]
        save_events(child_name, events)
        print("Event deleted successfully.")
    else:
        print("Invalid event index.")


# Main function
def main():
    clear_screen()
    while True:
        print("Welcome to School Organizer!\n")
        print("==============================")
        print("Main Menu:")
        print("1. Select Child")
        print("2. Add Child")
        print("3. Remove Child")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            clear_screen()
            child_name = select_child()
            if child_name:
                while True:
                    print(f"\nOrganizer for {child_name}")
                    print("1. Add Event")
                    print("2. View Events")
                    print("3. Delete Event")
                    print("4. Back to Main Menu")
                    child_choice = input("\nEnter your choice: ")
                    if child_choice == '1':
                        event = input("Enter event: ")
                        day = input("Enter day: ")
                        month = input("Enter month: ")
                        year = input("Enter year: ")
                        add_event(child_name, event, day, month, year)
                    elif child_choice == '2':
                        clear_screen()
                        view_events(child_name)
                    elif child_choice == '3':
                        event_index = int(
                            input("Enter event index to delete: "))
                        delete_event(child_name, event_index)
                    elif child_choice == '4':
                        clear_screen()
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '2':
            clear_screen()
            child_name = input("Enter child's name: ")
            add_child(child_name)
        elif choice == '3':
            clear_screen()
            child_name = input("Enter child's name to remove: ")
            remove_child(child_name)
        elif choice == '4':
            print("\nExiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
