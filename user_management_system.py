print("Program started!")
# Constants for field names
SRNO = 'srno'
NAME = 'name'
AGE = 'age'
GENDER = 'gender'
OCCUPATION = 'occupation'

# In-memory database
database = {'entries': []}


# === Utility Functions ===

def get_serial_no():
    return len(database['entries']) + 1


def get_entry_details():
    entry = {}
    entry[NAME] = input("Enter name: ")
    entry[AGE] = input("Enter age: ")
    entry[GENDER] = input("Enter gender: ")
    entry[OCCUPATION] = input("Enter occupation: ")
    return entry


def validated_entry():
    entry = get_entry_details()
    if not entry[AGE].isdigit():
        print("Invalid age. Entry cancelled.")
        return None
    return entry


def display_entry(entry):
    print(f"\nSRNO: {entry[SRNO]}")
    print(f"Name: {entry[NAME]}")
    print(f"Age: {entry[AGE]}")
    print(f"Gender: {entry[GENDER]}")
    print(f"Occupation: {entry[OCCUPATION]}")


def display_all_entries():
    if not database["entries"]:
        print("\nNo entries found.")
        return
    for entry in database["entries"]:
        display_entry(entry)


def select_entry_and_value():
    options = {
        1: (SRNO, "serial number"),
        2: (NAME, "name"),
        3: (AGE, "age"),
        4: (GENDER, "gender"),
        5: (OCCUPATION, "occupation")
    }

    while True:
        print('\nSearch or update based on:')
        for key, (field, label) in options.items():
            print(f"{key}. {field.capitalize()}")
        try:
            choice = int(input("Enter your choice: "))
            if choice in options:
                field, label = options[choice]
                value = input(f"Enter {label}: ")
                return field, value
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# === Database Operations ===

def add_entry(entry):
    entry[SRNO] = get_serial_no()
    database['entries'].append(entry)


def search_entry(value):
    return next((e for e in database['entries'] if e[value[0]] == value[1]), None)


def update_entry(value, updated_entry):
    for idx, entry in enumerate(database['entries']):
        if entry[value[0]] == value[1]:
            updated_entry[SRNO] = entry[SRNO]
            database['entries'][idx] = updated_entry
            return True
    return False


def delete_entry(value):
    for entry in database['entries']:
        if entry[value[0]] == value[1]:
            database['entries'].remove(entry)
            return True
    return False


# === Main Menu ===

def main():
    print("===== Welcome To User Management System =====")
    while True:
        print("\nWhat would you like to do:")
        print("1. Add an entry")
        print("2. Update an entry")
        print("3. Delete an entry")
        print("4. Search an entry")
        print("5. Display all entries")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            entry = validated_entry()
            if entry:
                add_entry(entry)
                print("✅ Entry successfully added.")

        elif choice == 2:
            value = select_entry_and_value()
            entry = validated_entry()
            if entry:
                if update_entry(value, entry):
                    print("✅ Entry successfully updated.")
                else:
                    print("❌ Entry not found.")

        elif choice == 3:
            value = select_entry_and_value()
            if delete_entry(value):
                print("✅ Entry successfully deleted.")
            else:
                print("❌ Entry not found.")

        elif choice == 4:
            value = select_entry_and_value()
            result = search_entry(value)
            if result:
                display_entry(result)
            else:
                print("❌ Entry not found.")

        elif choice == 5:
            display_all_entries()

        elif choice == 6:
            print("👋 Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
