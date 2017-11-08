# 编写一个名为collatz()的函数，它有一个名为number 的参数。
# 如果参数是偶数，# 那么collatz()就打印出number//2，并返回该值。
# 如果number 是奇数，collatz()就打印并返回3 * number + 1。

# 然后编写一个程序，让用户输入一个整数，并不断对这个数调用collatz()，直到函数返回值1
# （令人惊奇的是，这个序列对于任何整数都有效，
# 利用这个序列，# 你迟早会得到1！既使数学家也不能确定为什么。
# 你的程序在研究所谓的“Collatz 序列”，它有时候被称为“最简单的、不可能的数学问题”）。


def collatz(number):
    global result
    result = (number % 2 == 0) and (number / 2) or (3 * number + 1)
    print(str(result))
    return result

print('Enter number:')
while True:
    try:
        number = int(input())
    except ValueError:
        print('The value must be an integer!')
        continue
    collatz(number)
    if result == 1:
        break
