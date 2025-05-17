import random 

def guess_number(x):
    randon_number = random.randint(1 , x)

    guess = 0 

    while guess != randon_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randon_number:
            print('Sorry, guess again. Too low.')
        elif guess > randon_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed the number {randon_number} correctly!!')

guess_number(10)