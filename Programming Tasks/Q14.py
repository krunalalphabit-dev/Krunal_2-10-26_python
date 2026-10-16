'''14. Menu loop
Create a repeating menu with options: greet, show help, and quit. Continue until quit is selected. Handle unknown
choices without ending the program.
Extension: Count the number of menu actions before quitting.'''

count = 0

while True:
    print("\n1. Greet")
    print("2. Show Help")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello! Welcome.")
        count += 1
    elif choice == "2":
        print("Choose 1 to greet, 2 for help, and 3 to quit.")
        count += 1
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

print("Total menu actions:", count)