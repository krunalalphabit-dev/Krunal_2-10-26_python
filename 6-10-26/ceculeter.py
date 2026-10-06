a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c  = int(input("Enter your choice:"))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


if c ==1:
    print(f"addition for {a} + {b} = {a+b}")

elif c == 2:
    print(f"subtraction for {a} - {b} = {a-b}")

elif c == 3:
    print(f"multiplication for {a} * {b} = {a*b}")

elif c == 4:
    print(f"division for {a} / {b} = {a/b}")

else:
    print("invalid choice")
