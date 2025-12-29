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


marks = []
is_running = True

def getMarks():
	while is_running:
		count = 0
		mark = int(input("Enter your marks (Code: 2131 to finish)"))

		if mark == "2131":
			break
		else:
			marks.append(mark)
			len(marks) == count
	return marks
#	print(f"{count} items")
#print(marks)
total_exams = len(marks)

def average():
	total = 0
	for mark in marks:
		total += mark
	print(f"Total: {total}")

	average = (total / total_exams)
	return average

print("Total number of exams: ",total_exams)

getMarks()
average()
