# user input for starting amount and menu-driven program for billing system and user in  add in item in the list and show total bill and total items to bill used in append function this code in used in some chegis then print in selected it itemes name  last user  select 6 option bill in list and total items to bill and total bill print in the last user select 6 option

total = int(input("Enter starting amount: "))
total_items = 0
items_name = []
final_bill = []

while True:
    print("=" * 20)
    print("1. Add Pasta - Rs. 100")
    print("2. Add Pizza - Rs. 200")
    print("3. Add Brownie - Rs. 80")
    print("4. Add Dosa - Rs. 60")
    print("5. Show Total Bill")
    print("6. Show Total items_name in bill")
    print("7. Exit")
    print("=" * 20)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        total += 100
        total_items += 1
        items_name.append(("Pasta", 100))
        print("Pasta added successfully!")

    elif choice == 2:
        total += 200
        total_items += 1
        items_name.append(("Pizza", 200))
        print("Pizza added successfully!")

    elif choice == 3:
        total += 80
        total_items += 1
        items_name.append(("Brownie", 80))
        print("Brownie added successfully!")

    elif choice == 4:
        total += 60
        total_items += 1
        items_name.append(("Dosa", 60))
        print("Dosa added successfully!")

    elif choice == 5:
        print("Your total bill is:", total)

    elif choice == 6:
        final_bill.append(items_name.copy())
        final_bill.append(("Total Items", total_items))
        final_bill.append(("Total Bill", total))

        print("Final Bill Stored in List:", final_bill)
        print("Total items to bill:", total_items)
        print("Items in the bill:")

        for item in items_name:
            print("-", item[0], "- Rs.", item[1])

        print("Total Bill:", total)

    elif choice == 7:
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice!")