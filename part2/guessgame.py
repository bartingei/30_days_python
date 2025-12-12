# guessing game

import random


guess = int(input("Enter a number between 1 and 10 "))

while True:

    luckyNum = random.randint(1,10)

    if luckyNum == guess:
        print("\t \tCongratulations! You WON!! ")
        break
    elif guess >= 11 or guess <= 0:
        print("number is out of bounds! enter a valid number")
        guess = int(input("Enter a number between 1 and 10 "))
    else:
        print(f"Wrong! please try again!")
        print("our lucky number was:", luckyNum)
        guess = int(input("Enter a number between 1 and 10 "))

print("\t \tThankyou for playing ")