# 10-4
# 访客名单 ：
# 编写一个while 循环，提示用户输入其名字。
# 用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。
# 确保这个文件中的每条记录都独占一行。

import os

if os.path.exists('guest_book.txt'):
    os.remove('guest_book.txt')

with open('guest_book.txt', 'w') as fs:
    while (True):
        name = input('plz input your name :')
        if name == 'q':
            break
        print('Hi, ' + name.title())
        fs.write(name.title() + ' arrived\n')
