print("\n STUDENT GRADE CALCULATOR")

name = input("Enter Student Name: ")

english = int(input("Enter English Marks: "))
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
computer = int(input("Enter Computer Marks: "))
hindi = int(input("Enter Hindi Marks: "))

total = english + maths + science + computer + hindi
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Student Name :", name)
print("Total Marks  :", total, "/500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
