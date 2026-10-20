'''P7. Coordinate grid (nested loops and patterns)
Read a positive row and column count. Print a rectangular grid where each cell displays its row and column
coordinates. Keep columns aligned and try a second version using row/column multiplication values.'''

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

if rows > 0 and cols > 0:
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(f"({i},{j})", end=" ")
        print()
else:
    print("Enter positive numbers")