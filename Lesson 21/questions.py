# Functions
# Author: Elliott Butt

import datetime
import random

temp_counter = 0
thr_counter = 0
days_counter = 0
invoice_counter = 0
guess_counter = 0


def cel_to_fahr(deg_celsius):
    # comment for description
    global temp_counter
    temp_counter += 1

    return 9 / 5 * deg_celsius + 32


def training_heart_rate(age, resting_rate):
    # comment for description
    global thr_counter
    thr_counter += 1

    return ((220 - age) - resting_rate) * 0.60 + resting_rate


def days_to_xmas(current_date):
    # comment for description
    global days_counter
    days_counter += 1

    til_xmas = datetime.datetime(datetime.date.today().year, 12, 25).date(
    ) - datetime.datetime.strptime(current_date, "%Y-%m-%d").date()

    if til_xmas.days > 0:
        return f"{til_xmas.days} day(s) til xmas"
    elif til_xmas == 0:
        return f"It's xmas!"
    else:
        return f"Christmas is {abs(til_xmas.days)} day(s) passed."


def invoice_age(comp_name, invoice_date, invoice_amt):
    # comment for description
    global invoice_counter
    invoice_counter += 1

    age = datetime.datetime.today() - datetime.datetime.strptime(
        invoice_date, "%Y-%m-%d")

    if age.days <= 30:
        print("OK")
    elif age.days >= 31 and age.days <= 60:
        print("Better think about paying")
    else:
        print("This one could be in trouble")

    return age.days


def gussing_game():
    # comment for description
    global guess_counter
    guess_counter += 1

    answer = random.randrange(1, 100)
    guesses = 0

    while True:
        guess = int(input("Guess a number between 1-100: "))
        guesses += 1

        if guess == answer:
            print("You won!")
            print(f"You guessed {guesses} times!")
            break
        elif guess > answer:
            print("You are too high")
        elif guess < answer:
            print("You are too low.")

        print("Try again!")


while True:
    print()
    print("Mo's Quick Problems - Main Menu")
    print(
        f"Session totals: Temp: {temp_counter:2d} THR: {thr_counter:2d} Days to Xmas: {days_counter:2d} Old Invoice: {invoice_counter:2d} Guess: {guess_counter}")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Determine Training Heart Rate")
    print("3. How many days to Christmas")
    print("4. How old is an invoice")
    print("5. Play my guessing game")
    print("6. Quit")
    print()

    try:
        choice = int(input("Enter choice (1-6): "))
    except:
        print("Must be 1-6. Re-enter.")
    else:
        if choice == 1:
            print()
            print(cel_to_fahr(30))
        elif choice == 2:
            print()
            print(training_heart_rate(32, 80))
        elif choice == 3:
            print()
            print(days_to_xmas("2023-12-25"))
        elif choice == 4:
            print()
            print(invoice_age("XYZ", "2023-10-01", 100.00))
        elif choice == 5:
            print()
            gussing_game()
        elif choice == 6:
            break
