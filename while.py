# while loop -  used to execute a block of code repeatedly as long as a condition is true

"""name = input("Enter your name: ")

while name == "":
    print("Name cannot be empty. Please enter your name.")
    name = input("Enter your name: ")
print(f"Hello, {name}!")


age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be negative. Please enter a valid age.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")"""

"""food = input("Enter your favorite food: (type q to quit) ")

while not food == "q":
    print(f"{food} is a great choice!")
    food =  input("Enter another favorite food: (type q to quit) ")

print("Thank you for sharing your favorite foods!")

"""

"""
num = int(input("enter a number between 1 and 10 " ))

while  num < 1 or num > 10:
    
    print("invalid number, please try again")
    num = int(input("enter a number between 1 and 10 "))
 
print(f"you entered {num}, thank you!")
"""

#compound interest calculator

"""
principle = 0

rate = 0

time = 0


while principle <= 0:    
    principle = float(input("Enter the principle amount (greater than 0): "))
    if principle <= 0:
        print("Principle amount must be greater than 0. Please try again.")
        principle = float(input("Enter the principle amount (greater than 0): "))

while rate <= 0 or rate > 100:
    rate = float(input("Enter the annual interest rate (0-100): "))
    if rate <= 0 or rate > 100:
        print("Interest rate must be between 0 and 100. Please try again.")
        rate = float(input("Enter the annual interest rate (0-100): ")) 

while time <= 0:
    time = int(input("Enter the time in years (greater than 0): "))
    if time <= 0:
        print("Time must be greater than 0. Please try again.")
        time = int(input("Enter the time in years (greater than 0): "))

print(f"Principle amount: ${principle:.2f}, /n Annual Interest Rate: {rate}%, \n Time: {time} years")

amount = principle * pow((1 + rate/100), time)

print(f"amount: {amount}")"""

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount "))
    if principle <= 0:
        print("Principle amount cannot be less than or equal to zero")
        principle = float(input("Enter the principle amount "))

while True:
    rate = float(input("Enter the rate in % "))
    if principle <= 0:
        print("rate amount cannot be less than or equal to zero")
        rate = float(input("Enter the rate in % "))

while True:
    time = float(input("Enter the time (in years) "))
    if time <= 0:
        print("Principle amount cannot be less than or equal to zero")
        time = float(input("Enter the time (in years) "))

print(f"principle: {principle}\n, rate: {rate},\n time: {time}\n ")