# constants
BASE_SALARY = 0.00
COMM_RATE_1 = 0.01
COMM_RATE_2 = 0.02
TAX_RATE = 0.20
EI_RATE = 0.028
CPP_RATE = 0.049

# inputs
first_name = input("Enter employee first name: ")
last_name = input("Enter employee last name: ")
emp_SIN = input("Enter employee SIN: ")
weekly_sales = input("Enter weekely sales: ")
med_benefits = input("Enter medical benefits (S/F/C): ").upper()

extra_deduct = input(
    "Enter if you want extra income tax deducted (Y/N): ").upper()
if extra_deduct == "Y":
    extra_amount = input("Enter the extra amount you would like deducted: ")

contribute_RRSP = input(
    "Enter if you want to make an RRSP contribution (Y/N): ").upper()
if extra_deduct == "Y":
    contribute_amt = input("Enter the amount to contribute: ")


def calc_commission(sales):

    if sales >= 10000.00:
        commission = sales * COMM_RATE_2
    elif sales > 5000:
        commission = sales * COMM_RATE_1
    else:
        commission = -(sales * 0.1)

    return commission


def calc_benefits(benefits):

    tax_benefits = 0

    if benefits == "S":
        tax_benefits += 52.00
    elif benefits == "F":
        tax_benefits += 135.00
    elif benefits == "C":
        tax_benefits += 13.00

    return tax_benefits


def calc_tax(gross_pay, deduct, extra_income_tax, RRSP, RRSP_amt):

    tax_income = gross_pay * TAX_RATE
    tax_EI = gross_pay * EI_RATE
    tax_CPP = gross_pay * CPP_RATE
    tax_RRSP = 0
    tax_extra = calc_benefits(med_benefits)

    if deduct == "Y":
        tax_income += extra_income_tax

    if RRSP == "Y":
        tax_RRSP += RRSP_amt

    tax_deductions = tax_income + tax_EI + tax_CPP + tax_RRSP + tax_extra

    return tax_deductions
