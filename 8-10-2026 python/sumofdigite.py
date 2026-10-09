n = int(input("Enter  your number : "))
sum = 0
r = 0
for i in range(4):
    r = n  % 10
    sum += r
    n //= 10
print(sum)