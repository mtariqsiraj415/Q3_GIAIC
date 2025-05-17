
my_list = ["Apple","Banana" , "Mango" , "Orange" , "Grapes"]

def accese_elements(my_list , index):
    """Return the element at the specifies index , or as error message if out of range"""
    if 0 <=index < len(my_list):
        return f"Elements {index} : {my_list[index]}"
    return "Index out of range"

def modify_element(my_list , index , new_value):
    """Modifies the element at the specified index with the new value."""

    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Element at index {index} modified from {old_value} to {new_value}"
    return "Index out of range"


def slice_list(my_list , start , end):
    """Return the new list containing the element from the start index to the end index (exclusive)."""
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list):
        return f"Sliced list : {my_list[start:end]}"
    return "Invalid slice indicates"


def list_game():
    print("\n Wellcoe to the list maniputlation")
    my_list = ["Apple","Banana" , "Mango" , "Orange" , "Grapes"]

    while True:
        print("Current list",my_list)

                
        print("Select an operation")
        print("1 : Access Element")
        print("2 : Modify Element")
        print("3 : Slice List" )
        print("4 : Quit")

        choice = input("Eter your choice (1-4) : ")
        if choice == "1":
            index = int(input("Enter the index of the element you want to acces : "))
            print(accese_elements(my_list , index))
        elif choice == "2":
            index = int(input("Enter the index of the element you want to modify: "))
            new_value = input("Enter the new value for the element : ")
            print(modify_element(my_list , index , new_value))
        elif choice == "3":
            start = int(input("Enter the start index for the slice : "))
            end = int(input("Eter the end index for the slice :  "))
            print(slice_list(my_list , start , end))
        elif choice == "4":
            print("Exiting the game")
            break
        else:
            print("Invalid choice. plese enter a number between : 1 to 4")





if __name__ == "__main__":
    list_game()