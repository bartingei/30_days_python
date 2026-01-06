#Given a list of numbers:
#Copy code
#Python
#numbers = [12, 7, 34, 2, 19, 45, 10]
#Write a program to:
#Find the largest number
#Find the smallest number
#Calculate the average#
#❌ Do not use max(), min(), or sum().
#👉 Concepts: loops, variables, math

import math

numbers = [12, 7, 34, 2, 19, 45, 10]
total = 0

for i in numbers:
	total += i
average = total / len(numbers)

print("total: ", total)
print("Average: ", average)

#print(help(math))
print(numbers)
# finding the largest and smallest number
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
	if num > largest:
		largest = num
	elif num < smallest:
		smallest = num

print(" largest : ", largest)
print(" smallest : ", smallest)
