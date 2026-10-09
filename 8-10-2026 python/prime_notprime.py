a = int(input("Enter your number: "))

if a > 1:
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            print("NOT PRIME")
            break
    else:
        print(f"{a} is PRIME number")
else:
    print("NOT PRIME")
