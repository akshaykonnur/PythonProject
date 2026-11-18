# Rock, Paper, Scissors game

import random

options = ["rock", "paper", "scissors"]
playing = True

while playing:

    player = None                        # everytime the game starts this will reset the player
    computer = random.choice(options)    # the computer will have random choice

    while player not in options:         # the loop will keep running until you choose the option from options variable
        player = input("Enter your choice (rock, paper, or scissors): ").lower()

    print(f"Player: {player} ")
    print(f"Computer: {computer} ")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":               # conditions of playing game
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "n":
        playing = False

print("Thank you for playing")