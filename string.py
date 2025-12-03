name = input("Enter your name: ")

length = len(name)
print(length)

result = name.find("a")
print(result)

#.rfind is to find from the right side/ from reverse
result = name.rfind("o")
print(result)

# .replace is to replace a character with another character
new_name = name.replace("a", "e")
print(new_name)

# .upper is to convert all characters to uppercase
upper_name = name.upper()
print(upper_name)

# .lower is to convert all characters to lowercase
lower_name = name.lower()
print(lower_name)

# .capitalize is to capitalize the first character of the string
capitalized_name = name.capitalize()
print(capitalized_name)

# .title is to capitalize the first character of each word in the string
title_name = name.title()
print(title_name)

# .strip is to remove leading and trailing whitespace
stripped_name = name.strip()
print(stripped_name)

# .count is to count the occurrences of a substring in the string
count_a = name.count("a")
print(count_a)
 
# .startswith is to check if the string starts with a specific substring
starts_with_a = name.startswith("A")
print(starts_with_a)

# .endswith is to check if the string ends with a specific substring
ends_with_e = name.endswith("e")    
print(ends_with_e)

#this is used to check if all characters in the string are alphabetic
#space is not considered as alphabetic
result = name.isalpha()
print(result)

#isdigit is used to check if all characters in the string are digits
result = name.isdigit() 
print(result)

#isspace is used to check if all characters in the string are whitespace
result = name.isspace()
print(result)


