import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│    ●    │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for ecid in range(num_of_dice):
    dice.append(random.randint(1, 6))

#for ecid in range(num_of_dice):
#    for line in dice_art.get(dice[ecid]):
#        print(line)

for line in range(5):
    for ecid in dice:   
        print(dice_art.get(ecid)[line], end = "")
    print()
    
for ecid in dice:
    total += ecid

print(f"Total: {total}")