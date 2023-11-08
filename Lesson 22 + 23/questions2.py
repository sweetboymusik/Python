import datetime


def payment_date(purchase_date):
    if purchase_date.day < 25:
        due_date = datetime.date(
            purchase_date.year, purchase_date.month + 1, 1)
    elif purchase_date.day >= 25:
        due_date = datetime.date(
            purchase_date.year, purchase_date.month + 2, 1)

    return due_date


print(payment_date(datetime.date(2023, 5, 25)))


def gross_pay(sales):
    base_salary = 350.00
    sales_quota = 5000.00
    bonus = 0

    if sales < sales_quota:
        base_salary -= (sales_quota - sales) * 0.10
    elif sales > sales_quota:
        base_salary += sales * 0.04

    if sales > 10000.00:
        bonus += 200.00

    if sales > 20000.00:
        bonus += 500.00

    gross_pay = base_salary + bonus

    return gross_pay


print(gross_pay(4000.00))
print(gross_pay(5500))


def cust_status(limit, balance, last_purchase_date):
    message = ""

    if balance < limit - 200:
        message = "OK"
    elif balance <= limit:
        message = "CHECK"
    elif balance > limit:
        message = "OVER"

    if (datetime.date.today() - last_purchase_date).days > 60:
        message += " - PURCH"

    if (datetime.date.today() - last_purchase_date).days > 30:
        message += " - PAY"

    return message


print(cust_status(2000, 2001, datetime.date(2023, 9, 1)))
