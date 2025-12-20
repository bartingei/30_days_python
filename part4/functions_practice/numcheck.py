number = int(input("Enter a number: "))

def check_num(number):
    if number == 0:
        return "Zero"
    elif number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"

print(check_num(number))