# defualts must be at the end of the paramaters list
def greet_customer(name="Nameless", num_apples=7):
    print(f"Hello, {name}")
    print(f"We have {num_apples} apples in stock.")


greet_customer("Elliott", 10)
greet_customer()

print("hello")
