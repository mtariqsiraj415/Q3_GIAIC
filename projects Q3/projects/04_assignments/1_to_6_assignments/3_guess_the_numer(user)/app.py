import random

print("Guess the number between 1 and 10")

number = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess number: "))
    if guess <= number:
        print("You Low Number!")
    elif guess >= number:
        print("You High Number!")
    else:
        print("You Win!")
        break

