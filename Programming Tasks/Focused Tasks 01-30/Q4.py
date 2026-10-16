'''04. Two-number calculator
Read two numbers and a menu choice for addition, subtraction, multiplication, division, or remainder. Print a readable
equation. Handle an invalid menu choice and prevent division/remainder by zero.
Extension: Add floor division and exponentiation.
'''
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Remainder (%)")
print("6. Floor Division (//)")
print("7. Exponentiation (**)")
choice = int(input("Enter your choice: "))

if choice == 1:
    print(a, "+", b, "=", a + b)
elif choice == 2:
    print(a, "-", b, "=", a - b)
elif choice == 3:
    print(a, "*", b, "=", a * b)
elif choice == 4:
    if b != 0:
        print(a, "/", b, "=", a / b)
    else:
        print("Cannot divide by zero")
elif choice == 5:
    if b != 0:
        print(a, "%", b, "=", a % b)
    else:
        print("Cannot find remainder with zero")
elif choice == 6:
    if b != 0:
        print(a, "//", b, "=", a // b)
    else:
        print("Cannot divide by zero")
elif choice == 7:
    print(a, "**", b, "=", a ** b)
else:
    print("Invalid choice")