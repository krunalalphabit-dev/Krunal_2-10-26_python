'''21. Star patterns
Read a positive row count and print (a) a left-aligned triangle and (b) an inverted left-aligned triangle using nested
loops. Build each row by repetition or an inner loop'''

n = int(input("Enter number of rows: "))

if n <= 0:
    print("Enter a positive number")
else:
    print("Left-aligned triangle:")
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    print("Inverted triangle:")
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()