max_lenght = 3

def shorten(lst):
    while len(lst) >= max_lenght:
        last_element = lst.pop()
        print(last_element)

    
def get_lst():
    lst = []
    element = input("Enter an element to add to the list : ")
    while element != "":
        lst.append(element)
        element = input("Enter an element to add to the list : ")
        
    return lst


def main():
    lst = get_lst()
    shorten(lst)

if __name__ == "__main__":
    main()