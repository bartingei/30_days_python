import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            return

        attempts -= 1

    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
