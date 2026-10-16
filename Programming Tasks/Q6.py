'''06. Username builder
Read first name, last name, and birth year. Build a lowercase username from the first name and last name, with a dot
between them and the final two digits of the birth year. Print the original components and final username.
Extension: Replace internal spaces in names with underscores.'''

first_name = input("Enter first name: ").strip().replace(" ", "_")
last_name = input("Enter last name: ").strip().replace(" ", "_")
birth_year = input("Enter birth year: ")

username = first_name.lower() + "." + last_name.lower() + birth_year[-2:]

print("First Name:", first_name)
print("Last Name:", last_name)
print("Birth Year:", birth_year)
print("Username:", username)