
def add():
    print("This Application for add two numbers")
    first_number = int(input("Enter your First number :"))
    second_number = int(input("Enter your Seconds number :"))
    total_sum = first_number + second_number
    print(f"The Total sum of {first_number} and {second_number} is  : {total_sum}")

if __name__ == "__main__":
    add()