'''26. Student profile (dictionary basics)
Create a dictionary for one student with ID, name, city, and course. Print each key/value pair, update the city, add an
email field, and safely look up a key that may not exist'''

student = {
    "ID": 101,
    "name": "Krunal",
    "city": "Rajkot",
    "course": "Python"
}

# Print each key and value
for key, value in student.items():
    print(key, ":", value)

# Update city
student["city"] = "Ahmedabad"

# Add email
student["email"] = "rahul@gmail.com"

# Safely look up a key
print("Phone:", student.get("phone", "Key not found"))

# Print updated dictionary
print("\nUpdated Student Profile:")
print(student)