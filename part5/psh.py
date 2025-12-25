# this is a production based project
# intended for testing git branch

import random
import string

char = " " + string.digits + string.punctuation + string.ascii_letters

#print(char)
char = list(char)
key = char.copy()
random.shuffle(key)

#print(key)

value = input("Enter the text you want to encrypt: ")
encryptedtxt = ""

#encryption
for letter in value:
	index = value.index(letter)
	encryptedtxt += key[index]

print(f" original: {value}")
print(f" encrypted text: {encryptedtxt}")

