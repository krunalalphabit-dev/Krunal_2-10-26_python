budget = 3000
shop_name = "Krunal Stationery Shop"

items = [
    {"id": 1, "name": "Pencil", "price": 10, "available": True},
    {"id": 2, "name": "Eraser", "price": 5, "available": True},
    {"id": 3, "name": "Notebook", "price": 50, "available": True},
    {"id": 4, "name": "Pen", "price": 20, "available": True},
    {"id": 5, "name": "Geometry Box", "price": 120, "available": True}
]

order = []

print("===================================")
print("     STATIONERY SHOP BILLING")
print("===================================")
print("Customer budget: Rs.", budget)

print("\nAvailable Stationery Items")
print("-----------------------------------")

for item in items:
    if item["available"] == True:
        status = "Available"
    else:
        status = "Not available"

    print("ID:", item["id"],
          "| Name:", item["name"],
          "| Price: Rs.", item["price"],
          "| Status:", status)


customer_name = input("\nEnter customer name: ")

while True:
    item_id = input("\nEnter item ID (0 to finish): ")

    if not item_id.isdigit():
        print("Invalid ID!")
        continue

    item_id = int(item_id)

    if item_id == 0:
        break

    found = False

    for item in items:
        if item["id"] == item_id:
            found = True

            if item["available"] == False:
                print("Item is not available.")
                break
            while True:
                quantity_input = input("Enter quantity: ")

                if not quantity_input.isdigit():
                    print("Invalid quantity!")
                    continue

                quantity = int(quantity_input)
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                else:
                    break
            if quantity > 0:
                line_total = item["price"] * quantity

                order.append({
                    "name": item["name"],
                    "price": item["price"],
                    "quantity": quantity,
                    "line_total": line_total
                })

                subtotal = 0

                for ordered_item in order:
                    subtotal = subtotal + ordered_item["line_total"]

                print("Item:", item["name"])
                print("Line total: Rs.", format(line_total ))
                print("Running subtotal: Rs.", format(subtotal))

            break

        