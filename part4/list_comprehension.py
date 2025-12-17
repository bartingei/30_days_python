# List comprehension  =  is a concise way to create a list in python
#                       it is compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]

#traditional way to write lists
"""doubles = []

for i in range(1,11):
    doubles.append(i * 2)

print(doubles)"""

# compact and easier method

doubles = [x * 2 for x in range(1,11)]
triples = [i * 3 for i in range(1,11)]
squares = [y * y for y in range(1,11)]

print("doubles ",doubles)
print("triples ", triples)
print("squares ", squares)

# working with lists
fruits = ["apple", "banana", "orange" , "coconut"]

fruits = [fruit.upper() for fruit in fruits]

firsts = []

fruit_chars = [fruit[0] for fruit in fruits]


print(fruits)
print(fruit_chars)

#working with the if condition

# a list of positive and negative numbers
numbers = [-1,10,31,-3,11,100,-82,-66, 54]

#since there is no need to modify the number we just return num... if there was a need to modify the numbers we would have written something such as (num * 2)
positives = [num for num in numbers if num >= 0]
print("positives: ",positives)

negatives = [num for num in numbers if num < 0]
print("negatives: ",negatives)

#checking for even numbers

evenNumbers = [num for num in numbers if num % 2 == 0]
print("even numbers: ", evenNumbers)

oddNumbers = [num for num in numbers if num % 2 == 1]
print("odd numbers: ", oddNumbers)


# creating a list of grades

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60 ]
print("Passing grades: ",passing_grades)