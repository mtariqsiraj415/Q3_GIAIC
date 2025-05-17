peturksbouipo:int = 16
stanlau:int = 15
mayengua:int = 48


def main():
    age:int = int(input("How old are you? "))
    if age >= peturksbouipo:
        print(f"Your age is {age}.you are eligible to vote in Peturksbouipo")
    else:
        print(f"Your age is {age}.you are not eligible to vote in Peturksbouipo")

    
    if age >= stanlau:
        print(f"Your age is {age}.you are eligible to vote in stanlau")
    else:
        print(f"Your age is {age}.you are not eligible to vote in stanlau")


    if age >= mayengua:
        print(f"Your age is {age}.you are eligible to vote in mayengua")
    else:
        print(f"Your age is {age}.you are not eligible to vote in mayengua")


if __name__ == "__main__":
    main()