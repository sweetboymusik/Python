# report 1 (my way)

# report headings
print(f"ACCOUNT NO      CUSTOMER NAME      PHONE NO")

# intitialize counters and accumulators
cust_counter = 0

# open file
f = open("Customers.dat", "r")

# process each line in file
for line in f:
    line_split = line.split(", ")

    cust_num = line_split[0].strip()
    cust_name = line_split[1].strip()
    phone_num = line_split[4].strip()

    # calculations (if any)

    # print detail line
    print_line = f"{cust_num:<5s}         {cust_name:^18s}   {phone_num:>8s}"
    print(print_line)

    # increment any counters and accumulators as needed
    cust_counter += 1

# close the file
f.close()

# print summary or footer (analytics data)
print("-" * 43)
print(f"TOTAL CUSTOMER LISTED: {cust_counter:>02d}")
