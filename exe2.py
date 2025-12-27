#Ask the user to enter a password and check:
#At least 8 characters
#Contains at least one digit
#Contains at least one letter
#Print “Strong password” or “Weak password”.

import string

password = input("Enter a password: ")

has_digit = any(char in string.digits for char in password)
has_letter = any(char in string.ascii_letters for char in password)
long_enough = len(password) >= 8

if has_digit and has_letter and long_enough:
    print("Strong password")
else:
    print("Weak password")

