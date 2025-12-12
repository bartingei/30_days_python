import random

dice_art = {
    1: ("+------------------+",
        "|                  |",
        "|                  |",
        "|                  |",
        "|         ●        |",
        "|                  |",
        "|                  |",
        "|                  |",
        "+------------------+"),

    2: ("+------------------+",
        "|                  |",
        "|    ●             |",
        "|                  |",
        "|                  |",
        "|                  |",
        "|             ●    |",
        "|                  |",
        "+------------------+"),

    3: ("+------------------+",
        "|                  |",
        "|   ●              |",
        "|                  |",
        "|        ●         |",
        "|                  |",
        "|             ●    |",
        "|                  |",
        "+------------------+"),

    4: ("+------------------+",
        "|                  |",
        "|                  |",
        "|   ●          ●   |",
        "|                  |",
        "|                  |",
        "|   ●          ●   |",
        "|                  |",
        "+------------------+"),

    5: ("+------------------+",
        "|                  |",
        "|   ●          ●   |",
        "|                  |",
        "|         ●        |",
        "|                  |",
        "|   ●          ●   |",
        "|                  |",
        "+------------------+"),

    6: ("+------------------+",
        "|                  |",
        "|  ●           ●   |",
        "|                  |",
        "|  ●           ●   |",
        "|                  |",
        "|  ●           ●   |",
        "|                  |",
        "+------------------+")
}

dice = []
total = 0
num_of_dice = int(input("Hom many dice? "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in dice:
    total += die

#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

#to print the die faces on a horizontal line

for line in range(9): #9 here represents 
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

print(f"total: {total}")

print(dice)