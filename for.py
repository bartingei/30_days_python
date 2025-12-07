# for loops are used to execute a block of code for a fixed number of times

#for i in range(1, 11):   # you state the starting point and the ending point + 1
    #print(i, "\t")

#counting backwards
"""for x in reversed(range(1,11)):   #enclose the range in the reversed function to count backwards
    print(x)"""

"""
#using step
for m in range(1, 21, 2):   #the output for this skips by 2 
    print(m)"""

"""credit_card = "1234-5678-9012-3456"

for i in credit_card:
    print(i)"""

for x in range(1,21):
    if x == 13:
        continue

    else:
        print(x)


fruits = ["mango", "pineapple", "Tomato", "Orange" ]
for f in fruits:
    print(f)

print("mango" in fruits)

