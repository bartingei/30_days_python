# functions = a block of reusable code
#              place () after the function name to invoke it
# return  =  is used to end a function and send the result back to the caller


"""


def greet(name):
    print(f"hello {name}")

greet(name)
"""

'''name = input("Enter your name ")

def song1():
    print("Happy birthday to you!")

def song2():
    print(f"Happy birthday dear {name} ")

song1()
song1()
song2()
song1()'''

"""def hello(name, age):
    print(f"hello {name}, you are {age} years old! ")

hello("johnpaul", 12)"""

char = "*"

def drawRect():
    for i in range(1, 6):
        for j in range(1,6):
            print(char, end=" ")
        print()
        
print("*" * 10, " Rectangle ", "*" * 10)
drawRect()

def drawTriangle():
    for k in range(0,6,1):
        for l in range(k):
            print(k, end=" ")
        print()

print("*" * 10, " Triangle ", "*" * 10)
drawTriangle()

#drawing inverted triangle

def invertedTriangle():
    for m in range(6,0,-1):
        for n in range(m):
            print(m , end=" ")
        print()

print("*" * 10, " inverted Triangle ","*" * 10)
invertedTriangle()