username = input("Enter your username: ")

length = len(username)
print(length)

if length > 12:
    print("Username too long")
elif username.find(" ") != -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain a number")
else:
    print("Username is valid")