'''P2. Four-operation practice (types and arithmetic)
Read two decimal numbers and print their sum, difference, product, quotient, and remainder where valid. Convert
inputs to float, explain in comments why % needs a non-zero second value, and handle zero safely.'''

a = float(input("Enter first decimal number: "))
b = float(input("Enter second decimal number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)
    # % needs a non-zero second value because modulo by zero is undefined.
    print("Remainder:", a % b)
else:
    print("Quotient: Cannot divide by zero")
    print("Remainder: Cannot calculate with zero") 