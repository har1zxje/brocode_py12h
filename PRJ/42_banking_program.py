def show_balance(balance):
    print("*********************")
    print(f"Ur balance is ${balance:.2f}")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("Not a valid amount")
        print("*********************")
        return 0
    else:
        print("*********************")
        print(f"U have successfully deposited ${amount}")
        print("*********************")
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter an amount to be withdrawn: "))
    print("*********************")
    if amount >balance:
        print("*********************")
        print("Insufficent funds")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Not a valid amount")
        print("*********************")
        return 0
    else:
        print("*********************")
        print(f"U have successfully withdrawn ${amount}")
        print("*********************")
        return amount

def main():
    balance = 0 
    is_running = True

    while is_running:
        print("*********************")
        print("---Banking Program---")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")

        choice = input("Enter ur choice(1 - 4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("Not a valid choice")
            print("*********************")

    print("*********************")
    print("Thank u for using this program! Have a nice day!")
    print("*********************")

if __name__ == '__main__':
    main()