'''18. Factorial
Read a non-negative integer and compute its factorial with a loop. Define 0! as 1. Reject negative input.
PYTHON FUNDAMENTALS | FRESHER PRACTICE PACK 6
Extension: Also print each multiplication step.'''

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Negative number not allowed")
else:
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i
        print("Step:", fact, "=", end=" ")

    print("\nFactorial:", fact)