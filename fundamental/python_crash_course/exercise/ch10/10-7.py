# 10-7
# 加法计算器 ：
# 将你为完成练习10-6而编写的代码放在一个while 循环中，
# 让用户犯错（输入的是文本而不是数字）后能够继续输入数字。

count = 0
nums = []
while (count < 2):
    try:
        num = input('plz input a num : ')
        num = int(num)
        nums.append(num)
        count = count + 1
    except Exception:
        print('type error')

print('sum is ' + str(nums[0] + nums[1]))
