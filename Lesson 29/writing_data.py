# writing to a file example

import random


def main():
    outfile = open('data.txt', 'w')  # writes/overwrites data

    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    outfile.write(first_name + "\n")
    outfile.write(last_name + "\n")

    outfile.close()


def main2():
    outfile = open('salary.txt', 'a')  # appends data

    employee = input("Please enter employee name: ")
    salary = random.randint(35000, 50000)

    outfile.write(employee + "\n")
    outfile.write("$" + str(salary) + "\n")  # must convert number

    outfile.close()


main2()
