'''P9. Contact directory (dictionary operations)
Use a dictionary to store names and phone numbers. Provide a repeating menu to add/update, search, delete, list all
contacts, or quit. Handle missing names and empty directory safely.'''


contacts = {}

while True:
    print("\n1. Add/Update Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. List All Contacts")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == "4":
        if len(contacts) == 0:
            print("Directory is empty!")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")