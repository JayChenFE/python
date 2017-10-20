import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]


plt.plot(x_values,y_values)
plt.axis([0, 5500, 1, 1.25e11])
plt.show()