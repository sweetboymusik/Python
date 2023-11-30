f = open("Sales.dat", "r")

for SalesDataLine in f:
    SalesLine = SalesDataLine.split(",")
    EmpNum = SalesLine[0]
    EmpName = SalesLine[1]
    ItemCost = float(SalesLine[2])
    HST = float(SalesLine[3])
    TotalCost = float(SalesLine[4].strip())

    print(f"{EmpNum:<5s} {EmpName:<20} {ItemCost} {HST} {TotalCost}")

f.close()
