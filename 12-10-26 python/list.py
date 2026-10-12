name = ['Krunal', 'Rohit', 'Smit', 'Nilesh', 'Ramesh', 'Ketan', 'Jignesh', 'Hitesh', 'Nirav', 'Jayesh']

print(name[2])  # Output: Smit

name[2] = 'Smit Patel'  # Updating the value
print(name[2])  # Output: Smit Patel

name.append('Rakesh')  # Adding a new name to the list
print(name)


n = int(input("Enter the number of names you want to add: "))

for i in range(n):
    item = input("Enter items  name: ")
    name.append(item)
print(name) 