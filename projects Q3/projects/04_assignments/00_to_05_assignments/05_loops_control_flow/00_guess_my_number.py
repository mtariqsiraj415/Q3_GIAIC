import random

def main():
    secret_number = random.randint(1,100)
    print("I am thinking of a number btween (1 to 100)......")

    guess = int(input("Enter a guess : "))

    while guess != secret_number:
        if guess < secret_number:
            print("You guess is to low.")
        else:
            print("Your guess is to high.")
        guess = int(input("Enter a guess : "))
            
    print(f"Congratuation! the number was {secret_number}")

if __name__ == "__main__":
    main()
