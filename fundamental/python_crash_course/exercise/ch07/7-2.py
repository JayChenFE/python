# 7-2
#  餐馆订位 ：
# 编写一个程序，询问用户有多少人用餐。
# 如果超过8人，就打印一条消息，指出没有空桌；
# 否则指出有空桌。

number = input('plz input the number of People : ')
has_table = ' '
if int(number) > 8:
    has_table = ' not '

print('there are{}enough table for {} People'.format(has_table,number))
