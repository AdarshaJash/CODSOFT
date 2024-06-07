import sys
contacts = {}
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact {name} added successfully!")
def view_contacts():
    if not contacts:
        print(" No contacts found. ")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
def search_contact():
    search = input(" Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details['phone']:
            print(f"\nFound Contact: Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break
    if not found:
        print(" Contact not found. ")
def update_contact():
    name = input(" Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact {name}. Leave blank to keep current value.")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"Enter new email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"Enter new address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found.")
def delete_contact():
    name = input(" Please enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")
def main():
    while True:
        print("\nWelcome to the Python Contact Management System ")
        print(" 1. Add Contact ")
        print(" 2. View Contact List ")
        print(" 3. Search Contact ")
        print(" 4. Update Contact ")
        print(" 5. Delete Contact ")
        print(" 6. Exit ")
        choice = input(" Please enter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print(" Thank You for using the Python Contact Book ")
            print(" Designed by ADARSHA JASH ")
            sys.exit()
        else:
            print(" Invalid choice! Please enter a number between 1 and 6. ")
if __name__ == "__main__":
    main()