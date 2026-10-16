'''02. Type detective
Read a name, age, height in metres, and whether the student has prior coding experience (yes/no). Convert the
numeric inputs to suitable types. Print each value and its type. Convert the yes/no answer to a Boolean value.
Check: Age is an integer; height can include decimals.'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))
coding = input("Do you have coding experience? (yes/no): ").lower()

coding_experience = coding == "yes"

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Coding Experience:", coding_experience, type(coding_experience))