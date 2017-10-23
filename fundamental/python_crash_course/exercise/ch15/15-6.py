# 15-6
# 自动生成标签 ：
# 请修改die.py和dice_visual.py，
# 将用来设置hist.x_labels 值的列表替换为一个自动生成这种列表的循环。
# 如果你熟悉列表解析，
# 可尝试将die_visual.py和dice_visual.py中的其他for 循环也替换为列表解析。



import pygal

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
results.extend([(die_1.roll() + die_2.roll()) for roll_num in range(1000)])
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
frequencies.extend([results.count(value) for value in range(2,max_result + 1)])

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(value) for value in range(2,12)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')
