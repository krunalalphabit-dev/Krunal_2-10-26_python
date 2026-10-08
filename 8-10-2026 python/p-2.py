for i in range(5):
    for j in range(5):
        if j == i or j == 4 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()