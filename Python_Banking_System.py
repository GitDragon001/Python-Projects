from datetime import datetime

balance = 1000.00
transactions = []


def show_menu():
    print("\n===== PYTHON BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")


def check_balance():
    print(f"\nCurrent balance: ${balance:.2f}")


def deposit_money():
    global balance

    try:
        amount = float(input("Enter deposit amount: $"))

        if amount <= 0:
            print("Deposit amount must be greater than $0.")
            return

        balance += amount

        transactions.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"Deposit: +${amount:.2f} | Balance: ${balance:.2f}"
        )

        print(f"Deposit successful.")
        print(f"Your new balance is: ${balance:.2f}")

    except ValueError:
        print("Please enter a valid number.")


def withdraw_money():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: $"))

        if amount <= 0:
            print("Withdrawal amount must be greater than $0.")
            return

        if amount > balance:
            print("Insufficient funds.")
            return

        balance -= amount

        transactions.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"Withdrawal: -${amount:.2f} | Balance: ${balance:.2f}"
        )

        print("Withdrawal successful.")
        print(f"Your new balance is: ${balance:.2f}")

    except ValueError:
        print("Please enter a valid number.")


def show_transactions():
    print("\n===== TRANSACTION HISTORY =====")

    if not transactions:
        print("No transactions yet.")
    else:
        for number, transaction in enumerate(transactions, start=1):
            print(f"{number}. {transaction}")


while True:
    show_menu()

    try:
        select = int(input("\nChoose an option (1-5): "))
    except ValueError:
        print("Please enter a number between 1 and 5.")
        continue

    if select == 1:
        check_balance()

    elif select == 2:
        deposit_money()

    elif select == 3:
        withdraw_money()

    elif select == 4:
        show_transactions()

    elif select == 5:
        print("\nThank you for using the Python Banking System.")
        print("Goodbye!")
        break

    else:
        print("Please choose a number between 1 and 5.")
