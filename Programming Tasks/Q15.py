'''15. Running balance
Start with a user-entered balance. Repeatedly accept deposit, withdrawal, or quit. Reject non-positive amounts and
withdrawals larger than the current balance. Show the balance after each valid transaction'''

balance = float(input("Enter starting balance: "))

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Current balance:", balance)
        else:
            print("Amount must be positive")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be positive")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Current balance:", balance)

    elif choice == "3":
        print("Final balance:", balance)
        break

    else:
        print("Invalid choice")