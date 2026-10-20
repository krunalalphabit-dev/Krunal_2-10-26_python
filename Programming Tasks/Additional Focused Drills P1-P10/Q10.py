'''P10. Class results (nested list/dictionary data)
Store at least three students in a list of dictionaries; each record includes a name and a list of three marks. Print each
student's average and pass/fail result, then calculate the class average. Validate marks from 0 to 100.'''


students = [
    {"name": "Rahul", "marks": [80, 70, 90]},
    {"name": "Amit", "marks": [60, 65, 75]},
    {"name": "Priya", "marks": [90, 85, 95]}
]

total = 0
count = 0

for student in students:
    marks = student["marks"]

    if all(0 <= mark <= 100 for mark in marks):
        average = sum(marks) / 3
        print("Name:", student["name"])
        print("Average:", average)

        if all(mark >= 35 for mark in marks):
            print("Result: Pass")
        else:
            print("Result: Fail")

        total = total + average
        count = count + 1
    else:
        print("Invalid marks for", student["name"])

if count > 0:
    print("Class Average:", total / count)
