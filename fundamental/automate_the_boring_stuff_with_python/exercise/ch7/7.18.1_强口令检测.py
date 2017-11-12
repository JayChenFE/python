'''
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。

强口令的定义是：

长度不少于8 个字符，同时包含大写和小写字符，至少有一位数字。
你可能需要用多个正则表达式来测试该字符串，以保证它的强度。

'''
import re


def passStrengthTest(passWord):
    lowerRegex = re.compile(r'[a-z]')
    upperRegex = re.compile(r'[A-Z]')
    numRegex = re.compile(r'[0-9]')
    moLower = lowerRegex.search(passWord)
    moUpper = upperRegex.search(passWord)
    moNum = numRegex.search(passWord)
    if len(passWord) < 8:
        print('Your password is less than 8 characters which is too short.')
    elif not moLower:
        print('You need at least one lower case letter.')
    elif not moUpper:
        print('You need at least one upper case letter.')
    elif not moNum:
        print('You need at least one number.')
    else:
        print('Your password is strong!')
