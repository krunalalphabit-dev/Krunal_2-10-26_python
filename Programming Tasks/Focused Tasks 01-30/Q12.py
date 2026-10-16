'''12. Multiplication table (for loop)
Read an integer and print its multiplication table from 1 through 12. Align the output as equations.
Extension: Let the user choose the ending multiplier.'''

num = int(input("Enter a number: "))
end = int(input("Enter ending multiplier: "))

for i in range(1, end + 1):
    print(f"{num} x {i:2} = {num * i}")