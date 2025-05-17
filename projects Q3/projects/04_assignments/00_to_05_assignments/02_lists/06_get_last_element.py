def get_last_element(lst):
    print(lst[-1])


def get_list():
    lst = []
    element = input("Enter adn element to add to the list. ")
    while element != "":
        lst.append(element)
        element = input("Enter adn element to add to the list. ")
    return lst

def main():
    lst = get_list()
    get_last_element(lst)

if __name__ == "__main__":
    main()
