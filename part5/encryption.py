
# this is an encryption program, we aim to take inputs, encrypt it and decrypt it
# instead of rewriting the entire thing, we can import the string class elements 
# we can also add a space by placing an empty string

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
#print(chars)

# saving these  as list
chars = list(chars)

#lets create a key
key = chars.copy()

# shuffling the keys
random.shuffle(key)

# let us hide the key and characters
#print(f"\n chars: {chars}\n")
#print(f"key: {key}\n")

# encryption
plain_text = input("Enter a message to encrypt: ")
cypher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cypher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cypher_text}")

#decryption
cypher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cypher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cypher_text}")
print(f"Original message: {plain_text}")