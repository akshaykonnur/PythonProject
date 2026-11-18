# hangman in python

import random

words = ["apple", "banana", "cherry", "orange", "pineapple", "kiwi", "guava", "pomegranate", "dragonfruit", "coconut"]

# dictionary of key:()
hangamn_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):    # displays the hangman as the incorrect guesses
    print("-----------------------")
    for line in hangamn_art[wrong_guesses]:
        print(line)
    print("-----------------------")

def display_hint(hint):            # we'll have a string of hint, or hint is going to be the list of "_" characters for each letter of right guess we will flip the character
    print(" ".join(hint))

def display_answer(answer):        # we will display the correct ans either we win or lose
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:                # what if the letter is already guessed, so to avoid it
            print(f"The word {guess} was already guessed")
            continue                                # to skip the current iteration

        guessed_letters.add(guess)

        if guess in answer:                         # if our guess is in our answer, we will create a loop that will iterate once for each character within the ans
            for i in range(len(answer)):            # for every index of the length of my ans, for eg the ans is apple & and has 5 characters so i will iterate 5 times
                if guess == answer[i]:              # check during each iteration if our ans at the index of i is equal to our quess or its a match
                    hint[i] = guess                 # if we guessed the correct letter, then we are going to take out hint at that given index of i and set that equal to our guess
        else:
            wrong_guesses += 1

        if "_" not in hint:                          #  if there are no more blank line"_", it means you win
            display_man(wrong_guesses)               # it shows the final drawing
            display_answer(answer)                   # its shows the correct answer
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= len(answer)-1:         # the length of the hangman is 7(7 total keys) so subtracting 1 makes it 6, once we hit 6 we lose the game
            display_man(wrong_guesses)               # call the display_man function and pass in the wrong guesses
            display_answer(answer)                   # pass in the answer
            print("YOU LOSE")
            is_running = False


if __name__ == "__main__":
    main()
