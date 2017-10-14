# 4-12
# 使用多个循环 ：
# 在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for 循环来打印列表。
# 请选择一个版本的foods.py，在其中编写两个for 循环，将各个食品列表都打印出来。
my_pizzas = ['a','b','c','d']
friend_pizzas = my_pizzas[:]
my_pizzas.append('e')
friend_pizzas.append('f')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
