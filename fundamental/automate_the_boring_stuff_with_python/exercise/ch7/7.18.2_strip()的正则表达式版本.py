'''
写一个函数，它接受一个字符串，做的事情和strip()字符串方法一样。
如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
否则，函数第二个参数指定的字符将从该字符串中去除。
'''

import re


def remove_space(string):
    global stripped_str
    left_space_rex = re.compile(r'^\s*')
    right_space_rex = re.compile(r'\s*$')
    stripped_str = left_space_rex.sub('', string)
    stripped_str = right_space_rex.sub('', stripped_str)
    return stripped_str


remove_space('    here is the string    ')
print(stripped_str)
