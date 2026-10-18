'''20. Fibonacci sequence
Read how many Fibonacci terms to display. Print that many terms beginning with 0, 1. Handle 0 and 1 term requests
correctly; reject a negative count.'''

n = int(input("Enter number of terms: "))

if n < 0:
    print("Negative count not allowed")
else:
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c