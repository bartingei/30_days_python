# membership operators = are used to test whether a value or variable is fount in a sequence ( string, List, Tuple, Set or Dictionary)
#                       1. in
#                       2. not in


#testing out strings
"""word = "apple"
guesses = 0


while True:
    
    guess = input("guess a letter in the secret word \t ").lower()

    if guess in word:
        print(f"There is a letter {guess} in the word")
        guesses += 1
        
        
    else:
        print("\nLetter not found in word, please try again\n")
        guess = input("Try another letter \t ").lower()
        guesses += 1

print(f"Total number of guesses is : {guesses}")
"""


# testing out sets

"""students = {"JP", "mary", "Patience","Mark"}

students_lowercase = {name.lower() for name in students}

guess = input("Enter the name of a student ").lower()

if guess not in students_lowercase:
    print(f"{guess} not fount in the list")
else:
    print(f"{guess} is a student")"""

#using dictionaries

"""grades = {
    "Sandy" : "A",
    "Spongebob" : "B",
    "Patrick" : "C",
    "Squidward" : "D"
}

student = input("Enter the name of a student  ").capitalize()

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not found")"""

email = "johnpaulkibet3@gmail.com"

if "@" and "." in email:
    print("Valid email!")
else:
    print("Invalid Email!")