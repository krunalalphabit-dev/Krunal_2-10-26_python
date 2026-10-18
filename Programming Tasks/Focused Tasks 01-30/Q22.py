'''22. Number patterns
Read a positive row count. Print a right-triangle pattern where row 1 contains 1, row 2 contains 1 2, and so on. Then
print a second pattern where each row repeats its row number.'''

n = int(input("Enter number of rows: "))

if n <= 0:
    print("Enter a positive number")
else:
    print("Pattern 1:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("Pattern 2:")
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()