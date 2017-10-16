# 10-5
# 关于编程的调查 ：
# 编写一个while 循环，询问用户为何喜欢编程。
# 每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。

import os

if os.path.exists('reason.txt'):
    os.remove('reason.txt')

with open('reason.txt', 'w')as fs:
    while (True):
        print('\nwhy do u like programming?')
        reason = input('plz input your reason:')
        fs.write(reason + '\n')
        hasNext = input('is there next one?(y/n): ')
        if hasNext == 'n':
            break
