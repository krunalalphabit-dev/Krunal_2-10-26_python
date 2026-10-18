'''30. Cafe order (nested data and totals)
Represent a menu as a dictionary mapping numeric IDs to item details. Collect selected items into an order list; each
order entry should contain item name, unit price, and quantity. Calculate line totals and the subtotal, then print an
itemized receipt. Reject unknown IDs and non-positive quantities.'''

menu = {
    1: {"name": "Coffee", "price": 50},
    2: {"name": "Tea", "price": 20},
    3: {"name": "Sandwich", "price": 80},
    4: {"name": "Pizza", "price": 150}
}

order = []

while True:
    print("\nCafe Menu:")
    for item_id, item in menu.items():
        print(item_id, item["name"], "₹", item["price"])

    choice = input("Enter item ID (or done to finish): ")

    if choice.lower() == "done":
        break

    item_id = int(choice)

    if item_id not in menu:
        print("Invalid item ID!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be positive!")
        continue

    order.append({
        "name": menu[item_id]["name"],
        "price": menu[item_id]["price"],
        "quantity": quantity
    })

# Print receipt
print("\n------ CAFE RECEIPT ------")
subtotal = 0

for item in order:
    total = item["price"] * item["quantity"]
    subtotal += total

    print(item["name"], item["price"], "x", item["quantity"], "=", total)

print("--------------------------")
print("Subtotal: ₹", subtotal)