# dictionaries =   { } collections of {key : value} pairs that are ordered and unchangeable. No duplicates

capitals = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "Russia": "Moscow",
    "Australia": "Canberra",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Mexico": "Mexico City",
    "South Africa": "Pretoria",
    "Nigeria": "Abuja",
    "Egypt": "Cairo",
    "Argentina": "Buenos Aires",
    "South Korea": "Seoul",
    "Turkey": "Ankara",
    "Saudi Arabia": "Riyadh",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Poland": "Warsaw",
    "Greece": "Athens",
    "Thailand": "Bangkok",
    "Malaysia": "Kuala Lumpur",
    "Singapore": "Singapore",
    "New Zealand": "Wellington"
}


#print(dir(capitals))    # to print all the functions to work with a dictionary

#print(help(capitals))

print(capitals)

# we can use get method to find if a value exists in a dictionary

if capitals.get("japan"):
    print("\t That capital exists")
else:
    print("\t Capital does not exist")


# we can update the values of a dictionary
# you can also use this to add a value at the end of the dictionary

capitals.update(
    {
        "japan" : "hokkaido"
    }
)

print(capitals)


#to remove the last item from the dictionary

capitals.popitem()

print(capitals)

#to remove a specific item from the dictionary

#capitals.pop("USA")

#print(capitals)

# to clear the dictionary

#capitals.clear()

#print(capitals)

# to return the keys 
keys = capitals.keys()
print(keys)

#iterating through with a for loop

for key in capitals.keys():
    print(key)

values = capitals.values()

print(values)

for value in capitals.values():
    print(value)


items = capitals.items()

print(items)

for key, values in capitals.items():
    print(f" {key} => {value}")