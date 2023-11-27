# Program for local hotel conference center

# read defualts and set to program constants
f = open("defaults.dat", "r")

CON_NUM = int(f.readline())
HST_RATE = float(f.readline())
ROOM_S_RATE = float(f.readline())
ROOM_M_RATE = float(f.readline())
ROOM_L_RATE = float(f.readline())
BREAK_RATE = float(f.readline())
LUNCH_RATE = float(f.readline())
SUPP_RATE = float(f.readline())
COFFEE_RATE = float(f.readline())

f.close()

# main program
while True:

    # inputs
    client_name = input("Client name (END to exit): ")

    if client_name == "END":
        print("Have a good day!")
        break

    con_title = input("Conference title: ")
    start_date = input("Start date (YYYY-MM-DD): ")
    num_days = int(input("Number of days: "))
    max_attend = int(input("Max attendees: "))
    num_break = int(input("Number of breakfasts needed: "))
    num_lunch = int(input("Number of lunches needed: "))
    num_supp = int(input("Number of suppers needed: "))
    num_coffee = int(input("Number of coffee breaks needed: "))

    # calculations
    room_cost = 0
    if max_attend <= 30:
        room_cost = ROOM_S_RATE * num_days
    elif max_attend <= 100:
        room_cost = ROOM_M_RATE * num_days
    elif max_attend <= 250:
        room_cost = ROOM_S_RATE * num_days

    break_cost = (num_break * BREAK_RATE) * max_attend
    lunch_cost = (num_lunch * LUNCH_RATE) * max_attend
    supp_cost = (num_supp * SUPP_RATE) * max_attend
    coffee_cost = (num_coffee * COFFEE_RATE) * max_attend
    food_cost = break_cost + lunch_cost + supp_cost + coffee_cost

    subtotal = room_cost + food_cost
    taxes = subtotal * HST_RATE
    total = subtotal + taxes

    # output
    print("Output will be done later.")

    # write to conference.dat
    f = open("conference.dat", "w")

    f.write(f"{client_name}, ")
    f.write(f"{con_title}, ")
    f.write(f"{start_date}, ")
    f.write(f"{num_days}, ")
    f.write(f"{max_attend}, ")
    f.write(f"{num_break}, ")
    f.write(f"{num_lunch}, ")
    f.write(f"{num_supp}, ")
    f.write(f"{num_coffee}, ")
    f.write(f"{total}\n")

    f.close()

    # increment conference number
    CON_NUM += 1

    # write updated defaults to defaults.dat
    f = open("defaults.dat", "w")

    f.write(f"{CON_NUM}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{ROOM_S_RATE}\n")
    f.write(f"{ROOM_M_RATE}\n")
    f.write(f"{ROOM_L_RATE}\n")
    f.write(f"{BREAK_RATE}\n")
    f.write(f"{LUNCH_RATE}\n")
    f.write(f"{SUPP_RATE}\n")
    f.write(f"{COFFEE_RATE}\n")

    f.close()
