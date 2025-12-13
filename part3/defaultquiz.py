import time

"""def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)  #time.sleep will make the printed item to be printed one second at a time
    print("DONE! ")

count(0,10)

"""
#using default arguments

def count(end, start=10):  #the default argument should appear after the argument you are going to set the function call
    for x in range(start, end+1):
        print(x)
        time.sleep(1)  #time.sleep will make the printed item to be printed one second at a time
    print("DONE! ")

count(20)

