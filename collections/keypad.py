keypad = (
    (1 ,2 ,3 ),
    (4 ,5 ,6 ),
    (7 ,8 ,9 ),
    ("*",0,"#")
)

for key in keypad:
    for i in key:
        print( i, end=" ")
    print()