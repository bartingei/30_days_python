# conditional expression = A one line shortcut for the if-else statement
#                           Sometimes called a ternary operator 
#                           (a operator that takes three operands)
#                           Used to assign a value to a variable based on a condition

num = 5

age = 32

digit = 21

choice = "yes"

user_role = "user"

print("positive"if num > 0 else "negative")

print("Adult" if age >= 18 else "minor")

print("even" if digit % 2 == 0 else "odd")

status = "affirmative" if choice == "yes" else "negative"
print(status)

access_level = "full access" if user_role == "admin" else "limited access"
print("access level: ",access_level)