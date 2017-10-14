# 4-10
# 切片 ：
# 选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
#   打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
#   打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
#   打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。

num = [1,2,3,4,5,6,7]
print('The first three items in the list are:')
print(num[:3])

print('The middle three items in the list are:')
start_index = int((len(num) - 3) / 2)
print(num[start_index:start_index + 3])

print('The last three items in the list are:')
print(num[-3:])
