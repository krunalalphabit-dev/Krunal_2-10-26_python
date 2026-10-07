#1) marksheet with input method subjects and based on percentage use elif condition to decide which grade student will get

name = input("Enter your name: ")

maths = int(input("Enter marks obtained in Mathematics: "))
science = int(input("Enter marks obtained in Science: "))
english = int(input("Enter marks obtained in English: "))

total_marks = maths + science + english
percentage = total_marks / 300

print("\n------ Marksheet ---")
print("Name:", name)
print("Total Marks:", total_marks)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    


