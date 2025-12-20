
numbers = [12,23,43,54,65,67,87,98]

def summation():
    total = 0
    for number in numbers:
        print(number, end=" ")
        total += number
    print("\ntotal: ",total)

summation()