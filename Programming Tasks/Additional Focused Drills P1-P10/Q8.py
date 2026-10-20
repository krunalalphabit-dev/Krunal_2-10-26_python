'''P8. List statistics without helpers (list traversal)
Collect integers until the user types done. Use loops to calculate count, total, average, minimum, and maximum
without using sum, min, or max. Handle an empty list'''

numbers = []

while True:
    value = input("Enter an integer or done to stop: ")

    if value.lower() == "done":
        break

    numbers.append(int(value))

if len(numbers) == 0:
    print("List is empty")
else:
    count = 0
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for n in numbers:
        count = count + 1
        total = total + n

        if n < minimum:
            minimum = n

        if n > maximum:
            maximum = n

    average = total / count

    print("Count:", count)
    print("Total:", total)
    print("Average:", average)
    print("Minimum:", minimum)
    print("Maximum:", maximum)