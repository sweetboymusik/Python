def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome")


# must pass in all args
greet("Elliott", "Butt")
greet("John", "Smith")

print(greet("Ell", "Cooper"))  # is none, nothing returned

# perform - like great above
# return - like round()


def get_greeting(name):
    return f"Hi {name}"


# can do many things with the message
message = get_greeting("Elliott")
print(message)
open("content.txt", "w")

# keyword args


def increment(number, by):
    return number + by


# you can make code more readable by useing keyword args
print(increment(2, by=1))

# default args, optional params must come the the END of the params list


def increment2(number, inc=1):
    return number + inc


print(increment2(2))
print(increment2(2, 4))

# *args


def multiply(*numbers):
    print(numbers)  # returns a tuple

    total = 1
    for number in numbers:
        print(number)
        total *= number

    return total


print(multiply(2, 3, 4, 6))

# **args, can pass in key-value pairs


def save_user(**user):
    print(user)  # returns a dictionary
    print(user["name"])


save_user(id=1, name="John", age=22)


# scope
message3 = "z"  # this var is global


def greet3():
    message3 = "a"  # this only exists inside the function


def send_email(name):
    message3 = "b"


print(message3)  # prints z


# exercise
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"

    return input


print(fizz_buzz(30))
