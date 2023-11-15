BONUS_RATE = 0.01
DEDUCT_RATE = 0.17


def emp_bonus_status(total_sales):
    # calculate the emp bonus and status and return both

    bonus = total_sales * BONUS_RATE

    if total_sales < 5000.00:
        bonus -= (5000 - total_sales) * DEDUCT_RATE
    elif total_sales > 10000.00:
        bonus += 500.00

    if total_sales < 5000.00:
        status = "under"
    elif total_sales >= 5000.00 and total_sales <= 10000.00:
        status = "normal"
    else:
        status = "extraordinary"

    return bonus, status


print(emp_bonus_status(5000.00)[1])  # get values of tuple via index
