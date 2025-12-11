"""
    6.	Write a Python function that determines whether a given positive integer num is a perfect square.
      A number is considered a perfect square if it is the product of an integer multiplied by itself.
      Return True if num is a perfect square, otherwise return False.                                      
"""
import math

def is_perfect_square(num):
    root = math.sqrt(num)
    return root * root == num

num = int(input("Enter a number: "))
print(is_perfect_square(num))