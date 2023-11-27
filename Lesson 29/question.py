import datetime as dt

f = open("def.dat", "r")

CLAIM_NUM = int(f.readline())
HST_RATE = float(f.readline)
CURR_DATE = dt.datetime.now()

f.close()

while True:
    emp_name = input("Employee name: ")
    emp_num = input("Employee number: ")
    location = input("Location: ")
    start_date = "2023-11-06"
    end_date = "2023-11-09"
    num_days = 3
    car_status = "O"

    num_km = 0
    if car_status == "O":
        num_km = 1400

    if num_days <= 3:
        per_diem = num_days * 85.00
    else:
        per_diem = num_days * 100.00

    if car_status == "O":
        mileage = num_km * 0.10
    else:
        mileage = num_days * 56.00

    claim_amt = per_diem + mileage
    taxes = claim_amt * HST_RATE
    claim_total = claim_amt + taxes

    print(f"Claim num: {CLAIM_NUM}")
    print(f"Employee num: {emp_num}")
    print(f"Employee name: {emp_name}")
    print(f"Location: {location}")
    print(f"Claim total: ${claim_total}")

    # write data to a file called claims.dat
    f = open("claims.dat", "a")  # a for append

    f.write(f"{CLAIM_NUM}, ")
    f.write(f"{str(CURR_DATE)}, ")
    f.write(f"{num_days}\n")

    CLAIM_NUM += 1
    print("Claim data written.")

    cont = input("Continue?: ").upper()

    if cont == "N":
        break

f = open("def.dat", "w")
f.write(f"{CLAIM_NUM}\n")
f.write(f"{HST_RATE}\n")
f.close()

print("Thank you for using the claim processing program.")
