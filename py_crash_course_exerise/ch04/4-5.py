# 4-5 计算1~1 000 000的总和 ：创建一个列表，其中包含数字1~1 000 000，再使用min() 和max()
# 核实该列表确实是从1开始，到1 000 000结束的。另外，对这个列表
# 调用函数sum() ，看看Python将一百万个数字相加需要多长时间。

import time

nums = list(range(1, 1000001))

print("max is {:d}".format(max(nums)))

print('min is {:d}'.format(min(nums)))

start_time = time.time()

sum=sum(nums)

end_time = time.time()

print("time elapsed: {} ms".format(end_time - start_time))
print('sum is {}'.format(sum))
