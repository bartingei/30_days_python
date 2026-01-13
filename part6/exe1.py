#Write a program that:
#Takes an integer from the user
#Prints whether the number is positive, negative, or zero
#Also prints whether it is even or odd

num = int(input("Enter an integer: "))

if num == 0:
	print("number is 0")
elif num > 0:
	print(f"{num} is positive")
elif num < 0:
	print(f"{num} is negative")

if num % 2 == 0:
	print(f"{num} is even")
else:
	print(f"{num} is odd")

print("Thankyou fir using our program!")
