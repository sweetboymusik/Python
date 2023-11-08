apple_price = 0.75
bananna_price = 1.75

# always assign acums and ctrs to a starting value
total_due = 0  # accumulator
fruit_count = 0  # counter

more_fruit = input("Would you like to purchase fruit? ")

while more_fruit == "yes":
    fruit_type = input("Would you like an apple or bananas? ")

    if fruit_type == "apple":
        total_due += apple_price
    elif fruit_type == "bananas":
        total_due += bananna_price

    fruit_count += 1
    more_fruit = input("Would you like to purchase fruit? ")


print(total_due, fruit_count)
