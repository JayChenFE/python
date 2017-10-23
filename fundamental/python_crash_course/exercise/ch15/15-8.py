# 15-8
# 同时掷三个骰子 ：
# 如果你同时掷三个D6骰子，可能得到的最小点数为3，而最大点数为18。
# 请通过可视化展示同时掷三个D6骰子的结果。
import pygal
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()
# Make some rolls, and store results in a list.
results = []
results.extend([(die_1.roll() + die_2.roll() + die_3.roll()) for roll_num in range(10000)])
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies.extend([results.count(value) for value in range(3, max_result + 1)])

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [str(value) for value in range(3, 19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_3_visual.svg')
