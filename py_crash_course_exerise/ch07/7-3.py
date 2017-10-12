# 7-3
# 10的整数倍 ：
# 让用户输入一个数字，并指出这个数字是否是10的整数倍。

# py中没有 variable= expression ? b : c的三目运算符,替代为:
# (1) variable = a if expression else b
# (2)variable = (expression and [b] or [c])[0]
# (3) variable = expression and b or c

number = input('plz input a number and i wll tell u if it is the multiple of 10 : ')
is_multiple = int(number) % 10 == 0 and ' ' or ' not '
print('{} is{}the multiple of 10'.format(number,is_multiple))
