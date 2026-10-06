# create marksheet- 5 subjects using input method , I want total marks and percentage in output

python = int(input("Enter marks for Python: "))
java = int(input("Enter marks for Java: "))
c = int(input("Enter marks for C: "))
cpp = int(input("Enter marks for C++: "))
cn = int(input("Enter marks for CN: "))
total = python + java + c + cpp 

a = total / 5

print("Total Marks: ", total)
print("Percentage: ", a)