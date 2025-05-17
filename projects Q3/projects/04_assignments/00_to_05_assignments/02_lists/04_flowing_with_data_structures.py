def three_copy(lst,data):
    for i in range(3):
        lst.append(data)


def main():
    message = input("Enter a message to copy. ")
    lst =[]
    print("Before :" , lst)
    three_copy(lst , message)
    print("After :" , lst)

if __name__ == "__main__":
    main()
    