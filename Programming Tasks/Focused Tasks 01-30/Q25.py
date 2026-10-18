'''25. Unique guest list
Collect names until the user types done. Keep a list without duplicate names, preserve insertion order, and allow a
user to remove a name. Explain what happens if the name is not found.'''

guests = []

while True:
    name = input("Enter guest name (or done to stop): ")

    if name.lower() == "done":
        break

    if name not in guests:
        guests.append(name)
    else:
        print("Name already exists!")

print("\nGuest List:", guests)

remove_name = input("Enter name to remove: ")

if remove_name in guests:
    guests.remove(remove_name)
    print("Name removed successfully!")
else:
    print("Name not found in the guest list.")

print("Final Guest List:", guests)