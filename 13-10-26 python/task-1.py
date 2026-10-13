# 1) using the dictionary, tuple and list -> create and handle the billing system ( if I select something from the menu then it should get appended in the list and print total items that the user has bought at the end)

# Billing System using Dictionary, Tuple and List

items_name = []
total = 0
final_bill = []

menu = {
    1: ("Pasta", 100),
    2: ("Pizza", 200),
    3: ("Brownie", 80),
    4: ("Dosa", 60)
}

while True:
    print("\n1. Pasta - Rs. 100")
    print("2. Pizza - Rs. 200")
    print("3. Brownie - Rs. 80")
    print("4. Dosa - Rs. 60")
    print("5. Show Total Bill")
    print("6. Final Bill")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice in menu:
        item = menu[choice]
        items_name.append(item)
        total += item[1]
        print(item[0], "added successfully!")

    elif choice == 5:
        print("Total Bill: Rs.", total)

    elif choice == 6:
        final_bill.append(items_name.copy())
        final_bill.append(("Total Items", len(items_name)))
        final_bill.append(("Total Amount", total))

        print("\nFinal Bill Stored in List:")
        for bill in final_bill:
            print(bill)

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")