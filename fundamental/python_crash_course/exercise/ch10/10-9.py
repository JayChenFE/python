# 10-9
# 沉默的猫和狗 ：
# 修改你在练习10-8中编写的except 代码块，让程序在文件不存在时一言不发。

file_name = 'cat.txt'
try:
    print('CATS:')
    with open(file_name) as fs:
        print(fs.read().rstrip())

    # file_name = 'dog.txt'
    filename = 'dog1.txt'
    print('\nDOGS:')
    with open(file_name) as fs:
        print(fs.read().rstrip())

except FileNotFoundError:
    # print('can not find ' + file_name)
    pass
