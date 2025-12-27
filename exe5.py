#Guess the Word Game
#Store a secret word (e.g. "python")
#Ask the user to guess the word
#Keep asking until they guess correctly
#Count and display how many attempts it took


clue = "snake"
print(clue)

count = 0
is_running = True
incorrects = []
while is_running:
	guess = input("Guess a word: ")

	if guess != "python":
		count += 1
		incorrects.append(guess)
		print("Incorrect, please try again \n")
	else:
		print("CONGRATULATIONS!! 🎉")
		count += 1
		print(f"Total attempts: {count}")
		is_running = False

print(f"incorrect guesses: {incorrects}", end=" ")

