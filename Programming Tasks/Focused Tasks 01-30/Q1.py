'''01. Personal introduction
Ask for a person's name, city, and favorite subject. Print a neat three-line introduction. Use meaningful variable names
and at least one print call with sep or an f-string.
Extension: Print a one-line version with a custom separator.'''

name = input("Enter your name: ")
city = input("Enter your city: ")
subject = input("Enter your favorite subject: ")

print("\nPersonal Introduction")
print(f"My name is {name}.")
print(f"I live in {city}.")
print(f"My favorite subject is {subject}.")

print(name, city, subject, sep=" | ")