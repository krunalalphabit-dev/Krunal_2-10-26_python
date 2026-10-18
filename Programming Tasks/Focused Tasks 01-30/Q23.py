'''23. Shopping list (list basics)
Ask how many grocery items to enter, collect names in a list, then display the numbered list and its length. Allow the
user to replace one item by its displayed position; validate the position.'''

items = []

n = int(input("How many grocery items? "))

for i in range(n):
    item = input("Enter item name: ")
    items.append(item)

print("\nShopping List:")
for i in range(len(items)):
    print(i + 1, items[i])

print("Total items:", len(items))

pos = int(input("Enter position to replace: "))

if pos >= 1 and pos <= len(items):
    new_item = input("Enter new item name: ")
    items[pos - 1] = new_item

    print("\nUpdated Shopping List:")
    for i in range(len(items)):
        print(i + 1, items[i])
else:
    print("Invalid position")