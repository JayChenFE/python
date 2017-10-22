# 15-2
#  彩色立方 ：
# 给你前面绘制的立方图指定颜色映射。

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Blues)
plt.axis([0, 5500, 1, 1.25e11])
plt.show()
