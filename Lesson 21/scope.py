# LEGB
# Local, Enclosing, Global, Built-in


# be careful with builtins
# python does not stop you from overwriting builtin functions
import builtins

print(dir(builtins))


x = "global x"
m = min([5, 1, 2, 4])


def test(z):
    # global x # specifies to use the global version of a var
    y = "local y"
    x = "local x"
    # print(y)
    print(x)
    print(z)


test("local z")
print(x)
# print(y) would throw an error

w = "hello"


def outer():
    w = "outer w"

    def inner():
        nonlocal w
        w = "hello"
        print(w)

    inner()
    print(w)


outer()
