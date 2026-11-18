import random

# print("WELCOME TO ROLLING DICE GAME")
""" 
while True:
    choice = input("press 'enter' to roll the dice or press 'q' to quit")
    choice = choice.strip()
    if choice == "q":
        print("thank you for playing")
        break
    elif choice == "":
        number = random.randint(1,6)
        print(f"you rolled a {number}")
    else:
        print("Invalid Input")
print("Thank you for playing","GAME OVER")
"""

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌────────┐"
"│        │"
"│        │"
"│        │"
"└────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("Enter number of dice: "))

#dice.append(random.randint(1,6))
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
print(dice)

# for die in range(num_of_dice):                       # the outer for loop will be incharge of num_of_dice
#    for line in dice_art.get(dice[die]):             # the inner for loop will be incharge of printing every tuple
#        print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end='')
    print()

for die in dice:
    total = (sum(dice))
print(total)

