#i created this on boxing day 2025

import time
import random

#print(help(time))

num = int(input("how many seconds of delay "))

for i in range(num, 0, -1):
	print(i)
	time.sleep(1)
songs = ["a","b","c","d","e","f","g"]

def play():
	while True:
		choice = input("Choose a song to play (a to g) ... (type exit to close player) ")
	
		if choice in songs:
			print("-"*5,"searching...", "-"*5)
			time.sleep(3)
			print("-" * 5, "song found", "-"*5)
			time.sleep(3)
			print(f" playing {choice}")
		elif choice == "exit":
			break
		else:
			print(f"Sorry we coudn't get that/n please try again! ")

play()
