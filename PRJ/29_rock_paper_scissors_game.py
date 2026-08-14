import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Draw!")
    elif player == "rock" and computer == "scissors":
        print("U win!")
    elif player == "paper" and computer == "rock":
        print("U win!")
    elif player == "scissors" and computer == "paper":
        print("U win!")
    else:
        print("U lose!")

    print("----------")
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Tks for playing")
 