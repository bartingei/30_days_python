import random

lowestNUm = 1
highestNum = 10
answer = random.randint(lowestNUm, highestNum)
guesses = 0
is_running = True  # we want to make is_running False whenever the user enters the correct guess

print("-" * 60)
print("\t \tPYTHON NUMBER GUESSING GAME")
print("-" * 60)

print(f"select a number between {lowestNUm} and {highestNum}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.strip() == "":
        print("Please input a number")
        continue
    
    if not guess.isdigit():
        print("The program will terminate because you are a fool.")
        break
    
    user_guess = int(guess)

    if user_guess < lowestNUm or user_guess > highestNum:
        print("Stop being a dumbass! Follow the rules!")
        continue
        
    if answer == user_guess:
        print("Congratulations you have WON!!!")
        break
    else:
        print("\n\nYOU LOST!... Please try again")
        guesses += 1
        #guess = input("Enter your guess: ")

print("-" * 60)
print(f"\tyour guess: {guess}\n \tour answer: {answer}")
print(f"\tTotal number of guesses: {guesses}")
print("-" * 60)