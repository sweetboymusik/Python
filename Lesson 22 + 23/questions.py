def spouse_age(age):
    return (age / 2) + 7


print(spouse_age(18))


def letter_grade(grade):
    if grade <= 100 and grade >= 80:
        return "A"
    elif grade < 80 and grade >= 70:
        return "B"
    elif grade < 70 and grade >= 60:
        return "C"
    elif grade < 60 and grade >= 50:
        return "D"
    elif grade < 50:
        return "F"


print(letter_grade(80))


def gross_pay(hours, hour_rate):
    if hours <= 40:
        pay = hours * hour_rate
    elif hours > 40:
        pay = (40 * hour_rate) + ((hours - 40) * (hour_rate * 1.5))

    return pay


print(gross_pay(42, 20))


def ideal_THR(age, resting_rate):
    return (((220 - age) - resting_rate) * 0.6) + resting_rate


print(ideal_THR(32, 80))


def bonus(sales):
    if sales < 5000.00:
        bonus = 0
    elif sales <= 10000.00 and sales >= 5000.00:
        bonus = sales * 0.01
    elif sales > 10000.00:
        bonus = (sales * 0.01) + 500.00

    return bonus


print(bonus(10000))

# test
