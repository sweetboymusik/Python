# use of nested lists here seems scuffed. Be careful adding complexity

import datetime

listing = []

while True:
    # this doesn't actually have to be a number. could just be a string
    try:
        list_num = int(input("Enter list number: "))
    except:
        print("Not a valid number. Please re-enter")

    if len(str(list_num)) != 9:
        print("Number must be 9 digits long. Please re-enter.")
    else:
        listing.append(["Listing Number", list_num])
        break

while True:
    street_add = input("Enter street address: ")

    if street_add == "":
        print("Cannot be blank. Please re-enter")
    else:
        listing.append(["Street Address", street_add])
        break

while True:
    try:
        num_bed = int(input("Enter number of bedrooms: "))
    except:
        print("Not a valid number. Please re-enter.")
    else:
        listing.append(["Number of bedrooms", num_bed])
        break

while True:
    try:
        num_bath = int(input("Enter number of bathrooms: "))
    except:
        print("Not a valid number. Please re-enter.")
    else:
        listing.append(["Number of bathrooms", num_bath])
        break

while True:
    try:
        square_footage = int(input("Enter total square footage: "))
    except:
        print("Not a valid number. Please re-enter.")
    else:
        listing.append(["Total square footage", square_footage])
        break

while True:
    listing_price = float(input("Enter listing price (0 to end): "))

    if listing_price == 0:
        break

    listing_date = input("Enter the listing date(YYYY-MM-DD): ")
    listing_date = datetime.datetime.strptime(listing_date, "%Y-%m-%d").date()

    listing.append(["Listing info", [listing_price, listing_date]])

while True:
    status_list = ["O", "P", "S"]

    status = input("Enter the listing status (O, P, or S): ").upper()

    if status == "":
        print("Cannot be empty. Please re-enter.")
    elif status not in status_list:
        print("Must be O, P, or S. Please re-enter.")
    else:
        if status == "O":
            status = "Open"
        elif status == "P":
            status = "Offer pending"
        elif status == "S":
            status = "Sold"

        listing.append(["Status", status])
        break

for key, val in listing:
    if key == "Listing info":
        print(f"{key}: {val[0]} {val[1]}")
    else:
        print(f"{key}: {val}")
