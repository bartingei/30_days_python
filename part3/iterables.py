# iterables = An object/collection that can return its elements ine at a time allowing it to be iterated over in a loop

'''numbers = [1,2,3,4,5]

for i in range(len(numbers)):
    print(i, numbers[i])
'''

#iterables include lists, sets, dictionaries, tuples etc.

"""fruits = {"Mango", "Banana", "Orange", "Apple", "Pineapple"}

for fruit in fruits:
    print(fruit)"""

"""name = "johnpaul kibet"

for i in name:
    print(i, end="")
    """

my_dictionary = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4
}
print("\n","*" * 30, "keys","*" * 30, "\n")
for key in my_dictionary.keys():
    print(key, end=" ")

print("\n","*" * 30, "values","*" * 30, "\n")
for value in my_dictionary.values():
    print(value , end=' ')

print("\n","*" * 30, "Key : values pairs","*" * 30, "\n")
for key,alue in my_dictionary.items():
    print(f"Key : {key} => Value : {value}" )