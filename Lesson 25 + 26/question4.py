num_list = []


def calc_list_total(list):
    total = 0

    for val in list:
        total += val

    return total


def calc_list_average(list):
    sum = calc_list_total(list)

    average = sum / len(list)

    return average


# there is a method for this... just writing my own for practice
def calc_list_max(list):
    max = list[0]

    for val in list:
        if val > max:
            max = val

    return max


# there is a method for this... just writing my own for practice
def calc_list_min(list):
    min = list[0]

    for val in list:
        if val < min:
            min = val

    return min


def calc_list_dups(list):
    seen_list = []
    dup_list = set()

    for val in list:
        if val in seen_list:
            dup_list.add(val)
        else:
            seen_list.append(val)

    if len(dup_list) == 0:
        dup_list = "No duplicates"
    return dup_list


while True:
    try:
        num = int(input("Enter a number to add to the list (-1 to exit): "))
    except:
        print("That's not a number, you silly goose. Try again :)")
    else:
        if num == -1:
            break

        num_list.append(num)


sorted = sorted(num_list)
sum = calc_list_total(num_list)
avg = calc_list_average(num_list)
min = calc_list_min(num_list)
max = calc_list_max(num_list)
dups = calc_list_dups(num_list)

print()
print(f"Numbers entered: {num_list}")
print(f"Sorted list: {sorted}")
print(f"Sum of all numbers: {sum}")
print(f"Average of all numbers: {avg}")
print(f"Min: {min}")
print(f"Max: {max}")
print(f"Duplicates: {dups}")
print()
