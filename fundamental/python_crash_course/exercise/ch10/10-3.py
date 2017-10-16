# 10-3
# 访客 ：
# 编写一个程序，提示用户输入其名字；
# 用户作出响应后，将其名字写入到文件guest.txt中。

import os

if os.path.exists('guest.txt'):
    os.remove('guest.txt')

with open('guest.txt', 'w') as fs:
    name = input('plz input your name :')
    fs.write(name)
