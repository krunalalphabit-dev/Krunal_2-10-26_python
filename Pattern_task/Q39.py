
rows = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1]
]

for row in rows:
    for j in range(6 - len(row)):
        print("  ", end="")
    for num in row:
        print(num, end="   ")
    print()
