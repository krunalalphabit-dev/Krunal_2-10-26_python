'''08. Number comparison
Read two integers. Report whether the first is greater, smaller, or equal. Also report whether both are positive, whether
either is zero, and whether they are different. Use comparison and logical operators'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("First is greater:", a > b)
print("First is smaller:", a < b)
print("Both are equal:", a == b)
print("Both are positive:", a > 0 and b > 0)
print("Either is zero:", a == 0 or b == 0)
print("Numbers are different:", a != b)