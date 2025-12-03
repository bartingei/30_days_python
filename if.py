#temp converter 
#1 degree celcius 

unit = input("is the temperature in (C)elsius or (F)arenheit? ").upper()

temp = float(input("Enter the temperature: "))

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}C is {converted}F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp}F is {converted}C")
else:
    print("invalid unit")