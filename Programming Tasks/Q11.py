'''11. Leap year and compact decision
Read a year and determine if it is a leap year using the Gregorian rules: divisible by 400, or divisible by 4 but not 100.
First write the full Boolean condition; then write the same decision using a conditional expression and compare
readability.'''

year = int(input("Enter a year: "))

# Full Boolean condition
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Conditional expression
result = "Leap Year" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "Not a Leap Year"
print(result)