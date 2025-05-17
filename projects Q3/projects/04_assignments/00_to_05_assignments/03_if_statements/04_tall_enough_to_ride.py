min_height:int = 50

def main():
    user_input =int(input("How tall are you? "))
    if user_input >= min_height:
        print("You are tail enoughbto ride.")
    else:
        print("You are not tail enough to ride may bhe next year.")


if __name__ == "__main__":
    main()