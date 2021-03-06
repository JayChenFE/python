# 10-8
# 猫和狗 ：
# 创建两个文件cats.txt和dogs.txt，
# 在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并打印一条友好的消息。
# 将其中一个文件移到另一个地方，并确认except 代码块中的代码将正确地执行。

filename = 'cat.txt'
try:
    print('CATS:')
    with open(filename) as fs:
        print(fs.read().rstrip())

    # filename = 'dog.txt'
    filename = 'dog1.txt'
    print('\nDOGS:')
    with open(filename) as fs:
        print(fs.read().rstrip())

except FileNotFoundError:
    print('can not find ' + filename)
