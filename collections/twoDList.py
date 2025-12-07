# this is a two dimensional List

fruits = ["apple", "orange", "banana","coconut"]

vegetables = ["celery", "carrots","potatoes"]

meats = ["chicken", "fish", "turkey"]

# all the above are one dimensional lists... to create a 2D lists you create a 1D lists and add all these other lists to it

groceries = [fruits, vegetables, meats]

for i in groceries:
    print(i, end=" ")
    print()

print(groceries[0]) # this will print out the first list

print(groceries[0][1])  #this will print out orange   

# to access an element on a 2D list u use two indexing operators

# 2D list example: school timetable

print()

#this can also work on tuples and even sets

timetable = [
    ("Math", "English", "Biology"),
    ("Physics", "Geography", "Chemistry"),
    ("History", "PE", "Computer Studies")

]

for lesson in timetable:
    print(lesson, end=" ")
print()

print(timetable[1])       # prints Tuesday's classes
print(timetable[1][2])    # prints Chemistry
