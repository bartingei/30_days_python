# *args         =        allows you to pass multiple non-key arguments
# **kwargs      =        allows you to pass multiple keyword-arguments
#                        * is an unpacking operator
#                        1. Positional, 2. default, 3. keyword, 4. arbitrary



print("-" * 100)
print("Kwargs and args are used to allow functions to take multiple values with no limitations")
print("-" * 100)



#using the normal function
"""def add(a,b):
    return a + b

print(add(1,2))"""

#using *args

def add(*args):
    total = 0
    for arg in args:        #iterating each item in the args
        total += arg
    return total

print(add(1,2,3,4,5,6,7))

print("\n","-" * 100)


#functions to display name

def display_name(*args):
#    fullName = []
    for arg in args:
#        fullName.append(arg)
        print(arg, end=" ")
    print()
#    for name in fullName:
#        return name
#    return "full Name: " ,fullName

display_name("\njohn", "paul")   #all these items are packed into a tuple

print("\n","-" * 100)

#kwargs

def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} => {value}")
    print()

address(street="njambi road",             #**kwargs save the elements as a dictionary
              city="Ongata",
              State="Rongai",
              zip="54321")

print("\n","-" * 100)


