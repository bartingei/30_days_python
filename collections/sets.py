#collection is a single "variable" used to store multiple values

# sets = {}  this is an unordered and immutable cannot include duplicates

#             it only allows adding or removing of items in the set

fruits = {"Mango", "Apple", "Banana", "Pineapple"}

fruits.add("Grapes")

#fruits.pop()
#fruits.remove("Apple")

print(dir(fruits))

for fruit in fruits:
    print(fruit, end=" ")
