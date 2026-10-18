'''29. Student marks register (list of dictionaries)
Store at least four students as dictionaries containing ID, name, and marks, inside a list. Print a roster, find a student
by ID, and calculate the class average. Handle an unknown ID.
PYTHON FUNDAMENTALS | FRESHER PRACTICE PACK 7
Extension: Find the highest scoring student and display their name and score.'''

students = [
    {"ID": 101, "name": "Krunal", "marks": 95},
    {"ID": 102, "name": "Amit", "marks": 72},
    {"ID": 103, "name": "Priya", "marks": 95},
    {"ID": 104, "name": "Neha", "marks": 68}
]

# Print student roster
print("Student Roster:")
for student in students:
    print(student["ID"], student["name"], student["marks"])

# Find student by ID
search_id = int(input("\nEnter student ID: "))
found = False

for student in students:
    if student["ID"] == search_id:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        found = True
        break

if not found:
    print("Student ID not found")

# Calculate class average
total = 0

for student in students:
    total += student["marks"]

average = total / len(students)
print("Class Average:", average)

# Find highest scoring student
highest = students[0]

for student in students:
    if student["marks"] > highest["marks"]:
        highest = student

print("Highest Scoring Student:", highest["name"])
print("Highest Marks:", highest["marks"])