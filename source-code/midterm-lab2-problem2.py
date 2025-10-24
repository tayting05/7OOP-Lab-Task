def show_balance(balance):
    print("********************************")
    print(f"Your balance is ${balance:.2f}")
    print("********************************")


def deposit(balance):
    amount = float(input("Enter an amount to be deposited: "))
    if amount > 0:
        balance += amount
    else:
        print("Invalid amount!")
    return balance


def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds!!!")
    elif amount <= 0:
        print("Invalid amount! Amount must be greater than 0.")
    else:
        balance -= amount
    return balance


def main():
    balance = 0
    while True:
        print("********************")
        print("      XYZ ATM      ")
        print("********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("********************")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance = deposit(balance)
        elif choice == 3:
            balance = withdraw(balance)
        elif choice == 4:
            print("Exiting Program.")
            break
        else:
            print("*************************************")
            print("Invalid input! Select a valid option.")
            print("*************************************")

    print("*************************************")
    print(" Thank you for using XYZ ATM ")
    print("*************************************")


main()
