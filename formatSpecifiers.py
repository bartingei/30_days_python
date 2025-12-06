# format spefifiers in Python = {value:flags}  formats valuse according to flags inserted

price1 = 3.14159
price2 = -902.65
price3 = 12.34
price4 = 1200

print(f" price1: {price1:.2f}, \n price2: {price2:.1f},\n price3: {price3:.3f}")  # this will format the float to 2 decimal places


# to have a total number of spaces
print(f" price1: {price1:10f}, \n price2: {price2:10f},\n price3: {price3:<8.3f}")  # total 8 spaces including decimal places

#to center the value in the space
print(f" price1: {price1:^10.2f}, \n price2: {price2:^10.2f},\n price3: {price3:^10.2f}")  # total 8 spaces including decimal places

#to have commas
print(f" price4: {price4:,}")  # this will format the float to 2 decimal places with commas

# to have commas, sign and total spaces
print(f" price2: {price2:+10,.2f}")  # this will format the float to 2 decimal places with commas and sign