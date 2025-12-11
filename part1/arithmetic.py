import math
# Arithmetic Operations

friends = 0
print(friends)

friends **= 1
print(friends)

# --- IGNORE ---
w = 144
x = 3.142
y = 5
z = -19

result = round(x)
print(result)

absolute = abs(z)
print(absolute)

power = pow(x,y)
print(power)

max_value = max(x,y,z)
print(max_value)

min_value = min(x,y,z)
print(min_value)

square_root = math.sqrt(w)
print(square_root)

pi = math.pi
print(pi)

top = math.ceil(pi)
print(top)

bottom = math.floor(pi)
print(bottom)

rundedOff = round(pi,2)
print("rounded off: ",rundedOff)

# --- IGNORE ---

# Modulus, Floor Division, and Exponentiation
modulus = 10 % 3
print(modulus)

floor_division = 10 // 3
print(floor_division)

exponentiation = 2 ** 3
print(exponentiation)

# Order of Operations
result_order = 10 + 3 * 2
print(result_order)

result_order_parentheses = (10 + 3) * 2
print(result_order_parentheses)
# --- IGNORE ---
# Area of a Rectangle
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width
print("The area is:", area)
# --- IGNORE ---

# Simple Interest Calculation
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)
# --- IGNORE ---

# Compound Interest Calculation
principal = float(input("Enter the principal amount: "))    
rate = float(input("Enter the annual interest rate (in %): "))    
time = float(input("Enter the time in years: "))
n = float(input("Enter the number of times interest is compounded per year: "))
amount = principal * (1 + (rate / (100 * n)))**(n * time)
compound_interest = amount - principal
print("The compound interest is:", compound_interest)
# --- IGNORE ---

# Loan Payment Calculation
principal = float(input("Enter the loan amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
monthly_rate = annual_rate / 100 / 12
years = int(input("Enter the loan term in years: "))
months = years * 12
monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate)**-months)
print("The monthly payment is:", monthly_payment)

