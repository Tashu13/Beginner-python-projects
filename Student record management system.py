students = []

while True:
    print("\nSTUDENT RECORD MANAGEMENT SYSTEM ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print(name, "added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(student)

    elif choice == "3":
        name = input("Enter student name to search: ")

        if name in students:
            print(name, "is found.")
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            students.remove(name)
            print(name, "deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
