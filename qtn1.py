#1.	Write a Python program where a function apply_operation 
# takes another function as a parameter along with two numbers,
#  and applies the passed-in function to those numbers.  (5 Marks)		

def apply_operation( func, num1, num2):
    result = func(num1, num2)
    print("result: ", result)

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

apply_operation(add,10,20)

apply_operation(multiply,10,20)



