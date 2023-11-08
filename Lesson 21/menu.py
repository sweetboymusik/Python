def main_menu():
    print("1. Do something good")
    print("2. Do something bad")
    print("3. Quit")

    while True:
        try:
            selection = int(input("Enter choice: "))

            if selection == 1:
                good()
                break
            elif selection == 2:
                bad()
                break
            elif selection == 3:
                break
            else:
                print("Invalid. Enter 1-3")
                main_menu()
        except ValueError:
            print("Ch0ose 1-3")

    exit


def good():
    print("good")
    anykey = input("Enter anything to return to main menu")
    main_menu()


def bad():
    print("bad")
    anykey = input("Enter anything to return to main menu")
    main_menu()


main_menu()
