total = int(input("Enter starting amount: "))

while True:
    print("=" * 20)
    print("1. Add Pasta - Rs. 100")
    print("2. Add Pizza - Rs. 200")
    print("3. Add Brownie - Rs. 80")
    print("4. Add Dosa - Rs. 60")
    print("5. Show Total Bill")
    print("6. Exit")
    print("=" * 20)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        total += 100
        print("Pasta added successfully!")

    elif choice == 2:
        total += 200
        print("Pizza added successfully!")

    elif choice == 3:
        total += 80
        print("Brownie added successfully!")

    elif choice == 4:
        total += 60
        print("Dosa added successfully!")

    elif choice == 5:
        print("Your total bill is:", total)

    elif choice == 6:
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice!")

