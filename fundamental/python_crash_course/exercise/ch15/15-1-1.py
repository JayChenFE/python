# 15-1
# 立方 ：
# 数字的三次方被称为其立方。
# 请绘制一个图形，显示前5个整数的立方值，
# 再绘制一个图形，显示前5000个整数的立方值。

import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values)

plt.axis([0, 6, 1, 220])
plt.show()

