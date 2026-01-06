# This is a basic py program
#  am trying to remind myself of **kwargs and *args

nums = []

def display_list(*args):
    total = 0
    for arg in args:
        total += arg
        nums.append(total)
    
    return "total: ", total

print(display_list(1,2,3,5,6,7,8))
