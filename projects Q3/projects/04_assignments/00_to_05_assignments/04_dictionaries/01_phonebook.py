def add_contact(phoenbook):
    name = input("Enter contact name : ")
    number =  input("Enter contact number : ")

    if name in phoenbook:
        print(f"{name} already exists in the phonebook.")
    else:
        phoenbook[name] = number
        print(f"{name} added to the phonebook.")


def serac_contact(phoenbook):
    name = input("Enter contact name to search : ")
     
    if name in phoenbook:
         print(f"{name} : {phoenbook[name]}")
    else:
        print(f"{name} is not found in phoebook")



def delete_contact(phonebook):
    name = input("Enter contact name to delete : ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted from the phonebook.")
    else:
        print(f"{name} not fount in phonebook")



def disply_contact(phonebook):
    if phonebook:
        print("\n Phonenook Contacts list")
        for name,number in phonebook.item():
            print(f"{name} : {number}")

    else:
        print("Phonebook is empty.")




if __name__  == "__main__":
    phonebook = {}

    while True:
        print("\n Phonebook Menu")
        print("1 : Add Contact")    
        print("2 : Search Contact")    
        print("3 : Delete Contact")    
        print("4 : Display Contact")    
        print("5 : Exit")

        choice = input("Enter your choice (1-5) : ") 

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            serac_contact(phonebook)
        elif choice == "3":
            delete_contact(phonebook)
        elif choice == "4":
            disply_contact(phonebook)
        elif choice == "5":
            print("Exiting phonebook Goodbye")
            break
        else:
            print("Invalid choice. Please enter a number (1 to 5).")