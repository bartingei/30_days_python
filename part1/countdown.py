# we are creating a countdown timer
import time

"""
my_time = int(input("Enter the time in seconds "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)

#time.sleep(5)   # the time is set here in seconds

print("Time is up")

"""

"""
#reversing the time

my_time = int(input("Enter the time in seconds "))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)

print("Reversal using a reversed function")

print(" Time is up! ")

#reversing using a step

my_time = int(input("Enter the time in seconds "))

for x in range(my_time, 0,  -1):
    print(x)
    time.sleep(1)

print("reversal using a step")

print(" Time is up! ")
"""

my_time = int(input("Enter the time in seconds "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600) % 60

    print(f'{hours:02} : {minutes: 02} : {seconds:02}')
    time.sleep(1)

#time.sleep(5)   # the time is set here in seconds

print("Time is up")

