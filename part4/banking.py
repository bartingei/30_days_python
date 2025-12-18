# python banking program

def show_bal(balance):
    print("-"* 60)
    print(f"Your balance is ${balance: .2f}")
    print("-"* 60)

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("-"* 60)
        print("THat is not a valid amount")
        print("-"* 60)
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount you want to withdraw: "))

    if amount > balance:
        print("-"* 60)
        print("Insufficient funds!")
        print("-"* 60)
        return 0
    elif amount < 0:
        print("-"* 60)
        print("Amount must be greater than 0")
        print("-"* 60)
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n","-"* 60)
        print("Banking Programme")
        print("-"* 60)

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit", "\n")
        

        try:
            choice = int(input("Enter a number (1-4): "))
        except ValueError:
            print("That is not a valid choice, please try again.")
            continue

        if choice == 1:
            show_bal(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance) 
        elif choice == 4:
            is_running = False
        else:
            print("That is not a valid choice,\nPlease Try again")
            
    print("\n")
    print("Thankyou... Have a nice day!")

if __name__ == "__main__":
    main()