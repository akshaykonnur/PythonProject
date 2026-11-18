import random

print("Welcome to Number Guessing Game")
lowest_num = 1
highest_num = 51
print(f"guess the number between {lowest_num} and {highest_num}")
secret_number = random.randint(lowest_num, highest_num)
guess = int(input("guess the number: "))
count = 10

while guess != secret_number:
    count = count - 1
    print(f"you have left {count} attempts")

    if count == 0:
        print("you have exhausted your attempts")
        break
    if guess > secret_number:
        print("you guessed too high, try lower")
        # guess = int(input("guess the number: "))
    else:
        print("you guessed too low, try higher")
    guess = int(input("guess the number: "))

if guess == secret_number:
    print("you guessed right")
    print("GAME OVER")



