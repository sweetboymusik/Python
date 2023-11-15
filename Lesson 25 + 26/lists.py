a = [3, 10, -1]

a.append(1)  # add to the list
a.append("Hello")  # can mix data types in a list
a.append([1, 2])  # list inside a list

a.pop()  # removes the last element in the list
a.pop()

a[0]  # gets a specific element
a[3]  # another specific element

a[0] = "first"  # change a specific element

print(a)

# exercise
b = ["banana", "apple", "microsoft"]

temp = b[0]
b[0] = b[2]
b[2] = temp

print(b)

# exercise 2 (same problem, different way)
b = ["banana", "apple", "microsoft"]

b[0], b[2] = b[2], b[0]  # easier way to swap to values

print(b)

###############################################

x = [2, 3, 5, 6, 1, 1, 3, 6, 7, 78, 8]

x.append(2)  # add to a list
x.insert(2, 10)  # insert value before specified index
x.remove(2)  # removes first instance of value
x.remove(x[2])  # removes third element

print(x[5:8])  # slices a portion of the list
print(x[-1])  # last element of list
print(x.index(1))  # gets index of value
print(x.count(1))  # gets number of instances of value
print(x.sort())  # wont work
x.sort()  # run before print, sort numerically

y = ["janet", "jessy", "alice", "bob", "joe"]
y.sort()  # sort alphabetically

print(x)
print(y)

###############################################

a = "Python"

for char in a:
    print(char)

b = ["we", "are", "learning", "python"]

for obj in b:
    print(obj)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i, num in enumerate(c):
    print(i, num)
