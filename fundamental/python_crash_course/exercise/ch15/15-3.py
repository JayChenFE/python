# 15-3
# 分子运动 ：
# 修改rw_visual.py，将其中的plt.scatter() 替换为plt.plot() 。
# 为模拟花粉在水滴表面的运动路径，向plt.plot() 传递rw.x_values和rw.y_values ，
# 并指定实参值linewidth 。
# 使用5000个点而不是50 000个点。
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values,linewidth=1)

    # Emphasize the first and last points.
    plt.plot(0, 0, c='green',linewidth=100)
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', linewidth=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
