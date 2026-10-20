'''P5. Multiples and count (for loop and condition)
Read a positive limit and a divisor. Loop from 1 through the limit, print all multiples of the divisor, and report their count
and sum. Reject a divisor of zero.'''

limit = int(input("Enter a positive limit: "))
divisor = int(input("Enter a divisor: "))

if limit <= 0:
    print("Limit must be positive")

elif divisor == 0:
    print("Divisor cannot be zero")

else:
    count = 0
    total = 0

    for i in range(1, limit + 1):
        if i % divisor == 0:
            print(i)
            count = count + 1
            total = total + i

    print("Count:", count)
    print("Sum:", total)