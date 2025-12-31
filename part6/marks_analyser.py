#Task
#Write a Python program using functions that does
# the following:
#Input marks for a given number of students
#Calculate the total marks
#Find the average marks
#Find the highest and lowest mark
# (without using max() or min())
#🛠️ Requirements
#You must create and use these functions:
#get_marks(n) → returns a list of marks
#calculate_total(marks) → returns total
#calculate_average(total, count) → returns average
#find_highest(marks) → returns highest mark
#find_lowest(marks) → returns lowest mark
# just a lil something to push to git 😂
#we shall continue this another day


marks = []

def getMarks():
    total_exams = int(input("How many exams do you want to enter? "))
    for i in range(total_exams):
        mark = int(input(f"Enter mark for exam {i+1}: "))
        marks.append(mark)
    return marks

def average():
    total = sum(marks)
    print(f"Total: {total}")
    if len(marks) == 0:
        return 0
    return total / len(marks)

getMarks()
print("Total number of exams: ", len(marks))
print(f"Average: {average()}")
