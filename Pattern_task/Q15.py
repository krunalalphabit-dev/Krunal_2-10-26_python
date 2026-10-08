for i in range(5, 0, -1):
    for j in range(i):
        print("*",end=" ")

    for j in range((5 - i) * 2):
            print(" ",end=" ")

    for k in range(i):
            print("*",end=" ")
    print()
    
    
    