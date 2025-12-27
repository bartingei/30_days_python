#Create a program with:
#Initial balance = 5000
#Menu options:
#Check balance
#Deposit money
#Withdraw money
#Exit
#Keep the program running until the user chooses Exit.

balance = 5000
is_running = True

def check_bal():
	print(f"current balance: {balance}")

def deposit(balance):
	amount = int(input("Enter the amount you want to deposit: "))

	if amount < 0:
		print("Amount must be greater than 0")
		return balance
	balance += amount
	return balance

def withdraw(balance):
	amount = int(input("Enter the amount you want to withdraw: "))
	if amount > balance:
		print("Insufficient balance")
		return balance

	if amount < 0:
		print("please enter a valid amount")
		return balance
	balance -= amount
	return balance

print("-" * 5, "Welcome to our Atm program", "-" * 5)
print("-" * 10,"\nMenu options","-" * 10)
while is_running:
	choice = int(input("1. Check balance \n2. Deposit \n3. Withdraw\n4. Exit \n"))
	if choice == 1:
		check_bal()
	elif choice == 2:
		balance = deposit(balance)
	elif choice == 3:
		balance = withdraw(balance)
	elif choice == 4:
		is_running = False
	else:
		print("Invalid choice!!")

