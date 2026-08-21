# Create a dictionary containing names and phone numbers
contacts = {
    "Alice": "9876543210",
    "Bob": "8765432109",
    "Charlie": "7654321098"
}

while True:
    print("\n--- Phone Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}, Phone: {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter contact name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == '5':
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
