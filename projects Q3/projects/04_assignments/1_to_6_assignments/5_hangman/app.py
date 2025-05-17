import random
from fruits import fruits

print("*********************** Welcome to Hangman! ***********************")
name = input("Enter your name: ")
print(f"Hello {name}! Let's start the game.")




word = random.choice(fruits)

total_chances = 7
guessed_word = "-"*len(word)

while total_chances !=0:
    print(guessed_word)
    letter = input("Guess a letter : ").upper()

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
                print(guessed_word)

        if guessed_word == word:
            print("Congratulation you won!!!")
            break

    else:
        total_chances -=1
        print("Incorrect guess")
        print("the remaining chances are : ",total_chances)

else:

    print("Game over")
    print("You lose")



print("the correct word : ",word)