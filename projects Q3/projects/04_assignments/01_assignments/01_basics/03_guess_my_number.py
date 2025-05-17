import random


#* ek randam number banye ga
randam_number = random.randint(0,99)

while True:

    #* User sey input ly ga number
    user_input = int(input("Guess the number : "))


    #* Condition check kry ga 
    if (user_input < randam_number ):
        print("Your guess is too Low")
    elif(user_input > randam_number):
        print("Your guess is too High")
    else:  
        print("Your guess is correct 🎉")
        break
