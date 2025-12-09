questions = (
    "How many elements are in the periodic table ",
    "Which animal lays the largest egg ",
    "What is the most abundant gas in the earth's atmosphere? ",
    "How many bones are in the human body? ",
    "Which planet in the solar system is the hottest? "
)

options = (
    ("A. 92", "B. 108", "C. 118", "D. 140"),
    ("A. Elephant", "B. Whale", "C. Ostrich", "D. Crocodile"),
    ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. 199", "B. 206", "C. 180", "D. 225"),
    ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter")
)


answers = ("C", "C", "B", "B", "B")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("-------------------------")
    print(question, end=" ")
    for option in options[question_num]:
        print("\n" , option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect \n")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1
    print()


print("--------------------")
print("      RESULTS       ")
print("--------------------")

print("answers ", end="")
for answer in answers:
    print(answer , end=" ")
print()

print("guess  ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(questions) * 100

print(f"Your score is {score}%")