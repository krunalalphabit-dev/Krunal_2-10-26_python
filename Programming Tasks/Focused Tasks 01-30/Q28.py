'''28. Inventory lookup (dictionary menu)
Use a dictionary whose keys are item codes and values are item names and prices. Repeatedly let a user look up an
item, add an item, update a price, or quit. Handle missing codes and invalid choices.'''

inventory = {
    "101": {"name": "Pen", "price": 20},
    "102": {"name": "Notebook", "price": 50}
}

while True:
    print("\n1. Look up item")
    print("2. Add item")
    print("3. Update price")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        code = input("Enter item code: ")

        if code in inventory:
            print("Name:", inventory[code]["name"])
            print("Price:", inventory[code]["price"])
        else:
            print("Item code not found")

    elif choice == "2":
        code = input("Enter new item code: ")

        if code in inventory:
            print("Item code already exists")
        else:
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))

            inventory[code] = {"name": name, "price": price}
            print("Item added successfully")

    elif choice == "3":
        code = input("Enter item code: ")

        if code in inventory:
            price = float(input("Enter new price: "))
            inventory[code]["price"] = price
            print("Price updated successfully")
        else:
            print("Item code not found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")