books = ["Python", "Java", "C++", "Data Science"]

while True:
    print("\n\tLIBRARY MANAGEMENT SYSTEM,")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Books:")
        for book in books:
            print(book)

    elif choice == "2":
        book = input("Enter the book name: ")

        if book in books:
            books.remove(book)
            print(book, "borrowed successfully.")
        else:
            print("Book is not available.")

    elif choice == "3":
        book = input("Enter the book name: ")

        if book not in books:
            books.append(book)
            print(book, "returned successfully.")
        else:
            print("Book is already in the library.")

    elif choice == "4":
        print("Thank you for visiting the library!")
        break

    else:
        print("Invalid choice. Please try again.")
