# 7-10
# 梦想的度假胜地 ：
# 编写一个程序，调查用户梦想的度假胜地。
# 使用类似于“If you could visit one place in the world, where would you go?”的提示，
# 并编写一个打印调查结果的代码块。

result = {}

while True:
    name = input('what is your name: ')
    place = input('If you could visit one place in the world, where would you go? :')
    result[name] = place

    question = input('hasNext one?(y/n):')
    if question == 'n':
        break

print('\n')

for name,place in result.items():
    print("{}'s favourite place is {}".format(name,place))
