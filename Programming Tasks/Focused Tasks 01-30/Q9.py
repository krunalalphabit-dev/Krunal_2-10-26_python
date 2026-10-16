'''09. Grade and pass decision
Read marks from 0 to 100. Print a grade band (A: 90-100, B: 75-89, C: 60-74, D: 40-59, F: below 40) and pass/fail
status. Reject values outside the valid range. Use an if/elif chain'''

marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
    print("Status: Pass")
elif marks >= 75:
    print("Grade: B")
    print("Status: Pass")
elif marks >= 60:
    print("Grade: C")
    print("Status: Pass")
elif marks >= 40:
    print("Grade: D")
    print("Status: Pass")
else:
    print("Grade: F")
    print("Status: Fail")