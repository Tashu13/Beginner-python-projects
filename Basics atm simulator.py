balance = 5000

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your current balance is ₹", balance)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("₹", amount, "deposited successfully.")
        print("Current Balance: ₹", balance)

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
            print("Current Balance: ₹", balance)
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using our ATM.")
        break

    else:
        print("Invalid choice. Please try again.")
