##5-11 序数 ：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
## 在一个列表中存储数字1~9。
## 遍历这个列表。
## 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。
## 输出内容应为1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th 和9th ，但每个序数都独占一行。
nums = tuple(range(1, 10))
suffix = ''
for val in nums:
    if val == 1:
        suffix = 'st'
    elif val == 2:
        suffix = 'nd'
    elif val == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    print(str(val) + suffix)
