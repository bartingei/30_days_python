# keyword arguments = an argument preceded by an identifier... it helps with readability, the order of arguments do not matter
# positional arguments order should be maintained before the keyword arguments 
import random

"""def hello(greeting, title, first, last):
    print(f"{greeting} {title}{ first} {last}")"""

#hello("hello", "Mr.", "JP", "Kibet")
"""hello("hello", title="Mr.", last="JP", first="Kibet")  # the order does not matter

"""
#printing numbers btw 1 and 10

"""for i in range(1,11):
    print(i, end=" ")   #end is a keyword argument 
print()

print("1","2","3","4","5", sep="-")"""

country = "+254"
area = random.randint(700, 799)
first = random.randint(1, 999)
last = random.randint(1, 999)
#function to generate a phone number
# we need country code, area code, first 3 digits and last 3 digits
 
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

print("Random number selected: \t", get_phone(country, area, first, last))


