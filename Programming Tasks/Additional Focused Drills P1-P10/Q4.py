'''P4. Shipping cost selector (conditions and logic)
Read order amount and delivery distance. Apply a free-shipping rule when the order is at least Rs. 1000, otherwise
charge Rs. 50 for up to 5 km and Rs. 100 beyond 5 km. Reject negative values and show the amount due.
'''

amount = float(input("Enter order amount (Rs.): "))
distance = float(input("Enter delivery distance (km): "))

if amount < 0 or distance < 0:
    print("Invalid input! Values cannot be negative.")

elif amount >= 1000:
    print("Shipping cost: Rs. 0")
    print("Amount due: Rs.", amount)

elif distance <= 5:
    print("Shipping cost: Rs. 50")
    print("Amount due: Rs.", amount + 50)

else:
    print("Shipping cost: Rs. 100")
    print("Amount due: Rs.", amount + 100)