# Todo list program
# Date written: November 14, 2023
# Author: Elliott Butt

# define list
todo_list = []


# define program functions
def display_list(list):
    print("TODO LIST")
    if len(list) > 0:
        for index, item in enumerate(list):
            print(f"{index+1}. {item}")
    else:
        print("List is empty.")


def add_item(list):
    val = input("Enter item to add: ")
    list.append(val)
    print(f"{val} has been added.")


# this needs validating... input the value, or index?
def delete_item(list):
    val = input("Enter item index to delete: ")
    print(f"{list[val - 1]} has been deleted.")
    list.remove(list[val - 1])


def display_num_list():
    list = []

    while True:
        val = int(input("Enter number to add to list (-1 to finish): "))

        if val == -1:
            break

        list.append(val)

    print()
    for num in list:
        print(num)

    print()
    list_dsp = ""
    for num in list:
        list_dsp += str(num) + ", "

    print(list_dsp.removesuffix(", "))


def validate():
    PROV_LIST = ["AB", "BC", "MB", "SK", "ON", "QC",
                 "NB", "NL", "NS", "PE", "YT", "NT", "NU"]

    STATUS_LIST = ["S", "M", "W", "D", "O"]

    CODE_LIST = [2, 5, 7, 9]

    while True:
        prov = input("Enter a province (XX): ").upper()

        if prov not in PROV_LIST:
            print("Not in list. Please re-enter.")
        else:
            print("Input successful. Thank you.")
            break

    while True:
        mar_status = input("Enter marital status (S, M, W, D, or O): ").upper()

        if mar_status not in STATUS_LIST:
            print("Not in list. Please re-enter.")
        else:
            print("Input successful. Thank you.")
            break

    while True:
        try:
            code = int(input("Enter an item code (2, 5, 7, or 9): "))
        except:
            print("Not a valid input. Please re-enter.")
        else:
            if code not in CODE_LIST:
                print("Not in list. Please re-enter.")
            else:
                print("Input successful. Thank you.")
                break


# start program
while True:

    print("Mo's TODO List - Main Menu")
    print()
    print("1. Display list.")
    print("2. Add item to list.")
    print("3. Delete item from list.")
    print("4. Add numbers to a list and display.")
    print("5. Validate using a list.")
    print("6. Quit")
    print()

    choice = int(input("Enter choice (1-6): "))

    if choice == 1:
        display_list(todo_list)
    elif choice == 2:
        add_item(todo_list)
    elif choice == 3:
        delete_item(todo_list)
    elif choice == 4:
        display_num_list()
    elif choice == 5:
        validate()
    elif choice == 6:
        print("Thank you. Please use this program again!")
        break
    else:
        print("Input must be between 1 and 6. Try again.")
