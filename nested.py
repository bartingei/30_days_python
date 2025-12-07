#nested loops are loops within loops

"""for i in range(1,11):
    for j in range(1,11):
        print(i * j , end=" ")

    print()"""

#displaying numbers 1 to 9

"""for j in range(1,4):
    for i in range(1,10):
        print(i, end=" ")  # we use end to make the output be on the same line
    print()   # this blank print statement will print the output on a new line

"""
#program to take user input of the symbols , columns and rows they want for building a rectangle

rows = int(input("Enter the number of rows you want: "))
columns = int(input("Enter the number of columns you want: "))

symbol = input("Enter the type of symbol you want: ")

for i in range(0, rows):
    for j in range(0, columns):
        print(symbol , end=" ")
    print()  # this empty print function will make items to be printed on separate lines