correct_affermation = "I am capable of doing anything. I put my mind too."

def main():
    print("Wellcome to Wholesome Machine")
    user_input = input("Please type the following affermation :" + correct_affermation)

    if user_input == correct_affermation:
        print("That's right")
    else:
        print("That was not the affermation. Please try Again!")

if __name__ == "__main__":
    main()