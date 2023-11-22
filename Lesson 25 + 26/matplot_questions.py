import matplotlib.pyplot as plt

x = []
y = []

# for i in range(-100, 101):
#     x_point = i
#     y_point = (3 * i) - 4

#     x.append(x_point)
#     y.append(y_point)

# for i in range(-100, 101):
#     x_point = i
#     y_point = (2 * (i) ^ 2) + (4 * i) - 5

#     x.append(x_point)
#     y.append(y_point)

# for i in range(-100, 101):
#     x_point = i
#     y_point = ((5 * i) + 3) ^ 2

#     x.append(x_point)
#     y.append(y_point)

for i in range(0, 101):
    x_point = i
    y_point = (2 * i + 3)**(1/2)

    x.append(x_point)
    y.append(y_point)


plt.title("EB's Graph")
plt.grid(True)
plt.plot(x, y)

plt.show()
