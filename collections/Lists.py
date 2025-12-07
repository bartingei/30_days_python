#collection is a single "variable" used to store multiple values

# lists - declared using []

pupils = ["John", "paul", "Linda", "Elvis"]

"""
students = pupils.copy()

students.append("Jacinta")

total_students = len(pupils)

print("total students: ", total_students)
"""

#printing out everything on the list we can use a for loop
"""


for student in students:
    print(student, end=" ")
"""

#pupils.insert(2, "Derrick")
#pupils.append("Ted")
#pupils.remove("John")
#pupils.sort()
#pupils.sort(reverse=True)
#pupils.reverse()

#to clear a list
#pupils.clear()

#printing index of a value
#print(pupils.index("paul"))

#counting number of items in a list
#print(pupils.count("Elvis"))

print(dir(pupils))   # this will show the methods for this code

for pupil in pupils:
    print(pupil, end=" ")