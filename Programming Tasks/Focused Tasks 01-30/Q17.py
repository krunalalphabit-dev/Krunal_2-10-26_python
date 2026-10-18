'''17. Digit sum and reverse
Read a non-negative integer. Using a loop and arithmetic only (no string conversion), calculate the sum of its digits
and its reversed value. Treat 0 correctly.'''

num = int(input("Enter a non-negative integer: "))

temp = num
digit_sum = 0
reverse = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Sum of digits:", digit_sum)
print("Reversed number:", reverse)