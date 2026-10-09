'''i = int(input("ENter vale under 10 : "))

while(i<10):
    print(i)
    i+=1'''

while True:
    # 2)using nested if condition loop and shorthand operator make bank deposit and withdraw system
    b = int(input("Enter your initial bank balance: "))

    if b > 0:
        print("Enter 1 for withdraw",1)
        print("Enter 2 for deposit",2)
        print("ENter 3 for exit")
    c = int(input("Enter the choise : "))


    if c == 1:
        w = int(input("Enter withdraw amout "))
        b -= w
        print(f"this new amout{b}")
    elif c == 2:
        d = int(input("Enter deposit amout "))
        b += d
        print(f"this new amout{b}")
    else:
        print("Number is not velidated")


