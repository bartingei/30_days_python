import random

lowestNum = 1
highestNum = 100
answer = random.randint(lowestNum, highestNum)
guesses = 0
is_running = True

print("-" * 60)
print("PYTHON GUESSING GAME")
print("-" * 60)

while is_running:

    guess = input(f"Enter a number between {lowestNum} and {highestNum}  ")

    if guess.isdigit():
        guess_num = int(guess)

        if guess_num < lowestNum or guess_num > highestNum:
            print("Enter a number withing the specified range! ")
            continue

        if guess_num < answer:
            print("number is too low")
        elif guess_num > answer:
            print("number is too high")
        elif guess_num == answer:
            print("Congratulations! You have WON!")
            guesses += 1
            break

    else:
        print("Invalid input... ")
        continue

print("\n")
print("-" * 60)
print(f"The answer was {answer}\n your guess{guess_num} ")
print(f"Total number of guesses: {guesses}")
print("-" * 60)
    