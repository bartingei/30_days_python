def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():                             # commenting out the main function and the if statement at the bottom
    print("This is script 1")           # will cause the script 2 which imports script 1 to run all codes of script 1
    favorite_food("pizza")              # in our case here, we only want to run these written codes only directly when we want to
    print("Goodbye! ")

if __name__ == "__main__":
    main()

# basically main is used to allow another file to run other codes within it but not within the main... anything but the main