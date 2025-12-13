# a functions application programme to display an invoice

"""def display_invoice(username, amount, dueDate):
    print(f"hello {username}")
    print(f"Your bill of ${amount} is due on {dueDate}")

display_invoice("johnpaul", 10000, "01/21/2026")
"""

"""def add(num1, num2):
    z = num1 + num2
    return z

print("z = ",add(10,20))

def subtract(num1, num2):
    z = num1 - num2
    return z

print("z = ", subtract(30,5))"""


def create_fullName(first, last):
    #capitalizing first name
    first_name = first.capitalize()
    last_name = last.capitalize()
    full_name = first_name + last
    return full_name

print("full name: ", create_fullName("johnpaul", " kibet"))