'''16. Nested loops: class attendance grid
Ask for the number of classes and students per class. For each student, ask for a name and attendance
(present/absent). Print one class summary at a time, including present and absent counts. Use nested loops and
counters.
Extension: Display a simple row of P and A markers for each class.'''

classes = int(input("Enter number of classes: "))
students = int(input("Enter students per class: "))

for i in range(1, classes + 1):
    present = 0
    absent = 0
    attendance = ""

    print("\nClass", i)

    for j in range(1, students + 1):
        name = input("Enter student name: ")
        status = input("Enter attendance (P/A): ").upper()

        if status == "P":
            present += 1
            attendance += "P "
        else:
            absent += 1
            attendance += "A "

    print("Attendance:", attendance)
    print("Present:", present)
    print("Absent:", absent)