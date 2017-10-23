# 15-9
# 将点数相乘 ：
# 同时掷两个骰子时，通常将它们的点数相加。请通过可视化展示将两个骰子的点数相乘的结果。

import pygal
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
results.extend([(die_1.roll() * die_2.roll()) for roll_num in range(1000)])
# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
frequencies.extend([results.count(value) for value in range(1,max_result + 1)])

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(value) for value in range(1,37)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6',frequencies)
hist.render_to_file('dice_visual_multi.svg')
