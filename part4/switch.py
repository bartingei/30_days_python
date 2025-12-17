#match-case statement (switch) : an alternative to using many 'elif' statements 
#                                 to execute some code if a value matches a 'case'
#                                 benefits: cleaner and syntax is more readable

#match case statements, similar to the switch case statements
"""
def day_of_the_week(day):
    match day:
        case "Sunday":
            return "it is Sunday"
        case "Monday":
            return "it is Monday"
        case "Tuesday":
            return "it is Tuesday"
        case "Wednesday":
            return "it is Wednesday"
        case "Thursday":
            return "it is Thursday"
        case "Friday":
            return "it is Friday"
        case "Saturday":
            return "it is Saturday"
        case _:
            return "Invalid day"

print(day_of_the_week("Sunday"))
"""

# a single | is used to represent a logical or in python

def is_weekend(day):
    """
    Returns True if the given day is a weekend ("Saturday" or "Sunday"), otherwise returns False.

    Args:
        day (str): Name of the day (e.g., "Monday", "Tuesday", etc.).

    Returns:
        bool: True if weekend, False otherwise.
    """
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        
print(is_weekend("Monday"))