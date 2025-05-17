# ---------------------------------------------------------------------------- #
#?                       Rock, Paper, Scissors game python                       #
# ---------------------------------------------------------------------------- #



'''


import random
list_names=["r","p","s"]

user_choice=input("choose in these = Rock, Paper, Scissor:")
computer_choice=random.choice(list_names)

print(f"user choice = {user_choice},computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("both chooses the same so both wins")
elif user_choice == "s"and computer_choice == "r" :
    print("comp wins")
elif user_choice == "r" and computer_choice == "s" :
    print("user wins 🎉")
elif user_choice == "p" and computer_choice == "r" :
    print("user wins 🎉")
elif user_choice == "r" and computer_choice == "p" :
    print("comp wins")
elif user_choice == "s" and computer_choice == "p"  :
    print("user wins 🎉")
elif user_choice == "p" and computer_choice == "s":
    print("comp wins")
else:
   print("wrong alphabet/none of these:sorry!")



'''



# ---------------------------------------------------------------------------- #



#?                       Rock, Paper, Scissors game python                       #


import random

print("************ Welcome to Rock, Paper, Scissors game ************")


print("""Rules:
     1: Paper VS Rock = Paper wins
     2: Rock VS Scissors = Rock wins
     3: Scissors VS Paper = Scissors wins
""")

list_namees = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose in these = Rock, Paper, Scissor: ")

user_choice = user_choice.capitalize()

computer_choice = random.choice(list_namees)

print(f"User choice = {user_choice}, Computer choice = {computer_choice}")


#conditions




while True:
    if user_choice == computer_choice:
        print("Both chooses the same so both wins")
    elif user_choice == "Scissors" and computer_choice == "Rock":
        print("Computer wins")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("User wins 🎉")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("User wins 🎉")
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("Computer wins")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("User wins 🎉")
    elif user_choice == "Paper" and computer_choice == "Scissors":
        print("Computer wins")
    else:
        print("Wrong alphabet/None of these: Sorry!")

    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        user_choice = input("Choose in these = Rock, Paper, Scissor: ")
        user_choice = user_choice.capitalize()
        computer_choice = random.choice(list_namees)
        print(f"User choice = {user_choice}, Computer choice = {computer_choice}")
    else:
        print("Thanks for playing! Have a great day!")
        break



print("Game Over!")


        


    
