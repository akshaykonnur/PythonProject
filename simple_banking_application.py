
balance = 0


def check_balance():
     print("--------------------------")
     print(f"Your balance is {balance}")
     print("--------------------------")

def deposit(amount):
    global balance
    if amount > 0:
        balance = balance + amount
    elif amount < 0:
        print("--------------------------")
        print("Invalid amount")
        print("--------------------------")

def withdraw(amount):
    global balance
    if amount > 0 and amount < balance:
        balance = balance - amount
    elif amount < 0:
        print("--------------------------")
        print("Invalid amount")
        print("--------------------------")
    elif amount > balance:
        print("--------------------------")
        print("Insufficient funds")
        print("--------------------------")


if __name__ == "__main__":

    while True:
        print("1. Check balance")
        print("2. Deposit the amount")
        print("3. Withdraw the amount")
        print("4. Exit")
        print("--------------------------")
        choice = input("Enter your choice(1-6): ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            print("--------------------------")
            amount = (float(input("Enter amount to deposit: ")))
            deposit(amount)
        elif choice == "3":
            print("--------------------------")
            amount = (float(input("Enter amount to withdraw: ")))
            withdraw(amount)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
    print()
    print("--------------------------")
    print("Thank you for banking with us")
    print("--------------------------")

