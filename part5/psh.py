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

#print(f" original: {value}")
#print(f" encrypted text: {encryptedtxt}")

print("-" * 10)
print("your text has been successfully encrypted")
print("-" * 10)
# decryption
decryptedtxt = ""

for j in encryptedtxt:
	index = encryptedtxt.index(j)
	decryptedtxt += value[index]

print("-" * 10)
print(" decryption successful")
print("-" * 10)
print(f" ENCRYPTED TEXT: {encryptedtxt}")
#print(f" decrypted text : {decryptedtxt}")

