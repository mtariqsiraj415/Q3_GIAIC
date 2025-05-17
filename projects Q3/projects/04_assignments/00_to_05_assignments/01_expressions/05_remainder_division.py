def reminder():
    num_1 :int = int(input("Enter an integer to by divided :"))
    num_2 :int = int(input("Enter an integer to divided by:"))
    quotient = num_1 // num_2
    reminder = num_1 % num_2
    print(f"The result of this divsion is { quotient} with a reminder of {reminder}")


if __name__ == "__main__":
    reminder()