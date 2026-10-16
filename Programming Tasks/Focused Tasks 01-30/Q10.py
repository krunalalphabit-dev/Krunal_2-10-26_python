'''10. Ticket eligibility (nested conditions)
Ask for age and whether the person has a student ID. Under 5: free entry. Ages 5-17: child ticket. Ages 18+: adult
ticket; apply a student discount only when a valid student ID is present. Reject negative age and display the final ticket
price using your own stated prices.
Extension: Add a senior discount and ensure discounts do not stack
'''
age = int(input("Enter your age: "))
student_id = input("Do you have a student ID? (yes/no): ").lower()

if age < 0:
    print("Invalid age")
elif age < 5:
    price = 0
    print("Free entry")
elif age <= 17:
    price = 100
    print("Child ticket")
elif age >= 60:
    price = 150
    print("Senior ticket")
else:
    price = 200
    if student_id == "yes":
        price = price * 0.8
        print("Student discount applied")
    else:
        print("Adult ticket")

print("Final ticket price: ₹", price)