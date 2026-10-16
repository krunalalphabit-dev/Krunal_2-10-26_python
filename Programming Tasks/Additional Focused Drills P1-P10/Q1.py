'''P1. Formatted receipt lines (output and variables)
Ask for a product name, unit price, and quantity. Print a tidy three-column receipt line using an f-string, alignment, and
a calculated line total. Keep each input and calculated value in a clearly named variable'''

product_name = input("Enter product name: ")
unit_price = float(input("Enter unit price: ₹"))
quantity = int(input("Enter quantity: "))

line_total = unit_price * quantity

print("\n---------- RECEIPT ----------")
print(f"{'Product':<15}{'Quantity':>8}{'Total':>12}")
print(f"{product_name:<15}{quantity:>8}{line_total:>12.2f}")
print("-----------------------------")