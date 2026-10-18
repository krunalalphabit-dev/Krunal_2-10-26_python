'''19. Prime checker
Read an integer and report whether it is prime. Numbers below 2 are not prime. Test possible divisors with a loop and
stop early once a divisor is found.
Extension: List all primes from 2 through a user-entered limit.'''

num = int(input("Enter an integer: "))

if num < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")

limit = int(input("Enter limit: "))

print("Prime numbers are:")
for num in range(2, limit + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")