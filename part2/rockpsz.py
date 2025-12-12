import random

options = ("rock", "paper", "scissors")
running = True

while running:
    print("-" * 60)
    print("ROCK PAPER SCISSORS GAME USING PYTHON")
    print("-" * 60)

    player = None
    computer = random.choice(options)

    # Ask until player enters a valid choice
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"\nPlayer:   {player}")
    print(f"Computer: {computer}\n")

    # Game Logic
    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You Lost!")

    # Play again?
    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again != "y":
        running = False  # Corrected
        print("\nThanks for playing!")

print("-" * 60)
print("GAME ENDED")
print("-" * 60)
