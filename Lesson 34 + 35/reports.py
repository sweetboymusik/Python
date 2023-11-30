import datetime as dt

f = open("CustExtra.dat", "r")

print("Cust No       Name                 Phone            Bal Due      Pay Date")
total_cust = 0
total_bal_due = 0

for line in f:
    line_split = line.split(",".strip())

    cust_num = line_split[0]
    cust_name = line_split[1]
    cust_phone = line_split[2]
    cust_bal = f"${float(line_split[3]):,.2f}"
    cust_due_date = line_split[9].strip()

    balance = float(line_split[3])
    date = dt.datetime.strptime(cust_due_date, "%Y-%m-%d").date()
    date_fmt = date.strftime("%b %d, %Y")

    print(f"{cust_num:5s}    {cust_name:20s} {cust_phone:12s}{cust_bal:>15s}    {date_fmt}")

    total_cust += 1
    total_bal_due += balance

print(
    f"Total customers: {total_cust}                                ${total_bal_due:>,.2f}")

f.close()

# report 2 - exception report

f = open("CustExtra.dat", "r")

total_over_limit = 0

for line in f:
    line_split = line.split(",".strip())

    cust_num = line_split[0]
    cust_name = line_split[1]
    cust_phone = line_split[2]
    bal_due = float(line_split[3])
    cred_limit = float(line_split[4])

    if cred_limit > bal_due:
        continue

    amt_over = 0.00
    if cred_limit < bal_due:
        amt_over = bal_due - cred_limit
        total_over_limit += 1

    cust_due_date = line_split[9].strip()
    pay_due = (cred_limit * 0.05) + amt_over

    print(f"{cust_num:5s}    {cust_name:20s} {cust_phone:12s}     ${cred_limit:>,.2f}   ${amt_over:>,.2f}   {cust_due_date}      {pay_due}")

f.close()
