import string
import random

name = input(" what is your name: ")
chars = string.punctuation + string.digits + string.ascii_letters

print(chars)

chars.shuffle

print(chars)
