'''13. Count and sum (while loop)
Keep asking for integers until the user enters 0. Print how many non-zero values were entered, their sum, and their
average. Do not divide when no values were entered.
Extension: Track the largest value as well'''

count = 0
total = 0
largest = None

num = int(input("Enter an integer (0 to stop): "))

while num != 0:
    count += 1
    total += num

    if largest is None or num > largest:
        largest = num

    num = int(input("Enter an integer (0 to stop): "))

print("Count:", count)
print("Sum:", total)

if count > 0:
    print("Average:", total / count)
    print("Largest:", largest)
else:
    print("No numbers entered")