import matplotlib.pyplot as plt

x_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis = [5, 16, 34, 56, 32, 56, 32, 12, 76, 89]

plt.title("Prices over 10 years")
plt.scatter(x_axis, y_axis, color='red', marker="s", label="item 1")

plt.xlabel("Time (years)")
plt.ylabel("Price (dollars)")

plt.grid(False)
plt.legend()

plt.show()

# x_axis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_axis1 = [5, 16, 34, 56, 32, 56, 32, 12, 76, 89]

# x_axis2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_axis2 = [53, 6, 46, 36, 15, 64, 73, 25, 82, 9]

# plt.title("Prices over 10 years")

# plt.scatter(x_axis1, y_axis1, color='darkblue', marker='x', label="item 1")
# plt.scatter(x_axis2, y_axis2, color='darkred', marker='x', label="item 2")

# plt.xlabel("Time (years)")
# plt.ylabel("Price (dollars)")

# plt.grid(True)
# plt.legend()

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# t = np.arange(0.0, 3.0, 0.01)
# s = np.sin(2.5 * np.pi * t)
# plt.plot(t, s)

# plt.xlabel('time (s)')
# plt.ylabel('voltage (mV)')

# plt.title('Sine Wave')
# plt.grid(True)

# plt.show()

# from matplotlib import pyplot as plt
# from matplotlib import style

# style.use('ggplot')

# x = [0, 1, 2, 3, 4, 5]
# y = [46, 38, 29, 22, 13, 11]

# fig, ax = plt.subplots()

# ax.bar(x, y, align='center')

# ax.set_title('Olympic Gold medals in London')
# ax.set_ylabel('Gold medals')
# ax.set_xlabel('Countries')

# ax.set_xticks(x)
# ax.set_xticklabels(("USA", "China", "UK", "Russia",
#                     "South Korea", "Germany"))

# plt.show()

# import matplotlib.pyplot as plt

# labels = ['Oranges', 'Pears', 'Plums', 'Blueberries']
# quantity = [38, 45, 24, 10]

# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# plt.pie(quantity, labels=labels, colors=colors, autopct='%1.f%%',
#         shadow=False, startangle=90)

# plt.axis('equal')

# plt.show()


labels = ['FreeBSD', 'NetBSD', 'Linux', 'Window', 'Apple']
quantity = [4, 3, 12, 6, 2]
explodes = [0.2, 0, 0, 0, 0]

plt.pie(quantity, labels=labels, explode=explodes, autopct='%1.1f%%')
plt.axis('equal')

plt.show()
# plt.savefig('piechart3.png')
