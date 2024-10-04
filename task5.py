contacts = {}

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':  # Add Contact
        name = input("\nEnter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts[name] = {"Phone": phone, "Email": email}
        print(f"\nContact '{name}' added successfully!")

    elif choice == '2':  # View All Contacts
        if not contacts:
            print("\nNo contacts available.")
        else:
            print("\n--- Contact List ---")
            for name, info in contacts.items():
                print(f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\n")

    elif choice == '3':  # Search Contact
        name = input("\nEnter the name to search: ")
        if name in contacts:
            info = contacts[name]
            print(f"\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}")
        else:
            print(f"\nContact '{name}' not found!")

    elif choice == '4':  # Update Contact
        name = input("\nEnter the name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contacts[name] = {"Phone": phone, "Email": email}
            print(f"\nContact '{name}' updated successfully!")
        else:
            print(f"\nContact '{name}' not found!")

    elif choice == '5':  # Delete Contact
        name = input("\nEnter the name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"\nContact '{name}' deleted successfully!")
        else:
            print(f"\nContact '{name}' not found!")

    elif choice == '6':  # Exit
        print("\nExiting Contact Book. Goodbye!")
        break

    else:
        print("\nInvalid choice, please try again.")
