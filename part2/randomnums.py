import random

print("Enter your guess to win a million dollar jackpot! 😁")
print("Enter a number between 1 and 10 👉")

while True:
    guess_input = input("Your guess: ")

    # Check if user pressed enter without typing anything
    if guess_input.strip() == "":
        print("Please enter a value! 🤦‍♂️")
        continue

    # Convert to number
    guess = int(guess_input)

    # Generate random number
    number = random.randint(1, 10)

    if number == guess:
        print("CONGRATULATIONS!!! 🎆🎆🎇🎇🎇🎇 \nYOU HAVE WON 🥳")
        break
    else:
        print(f"AW SNAP!! 😭 YOU LOST 💀💀")
        print(f"Our lucky number was: {number}")
        print("Try again!\n")

print(f"\nYour guess: {guess}")
print(f"Our lucky number: {number}")
