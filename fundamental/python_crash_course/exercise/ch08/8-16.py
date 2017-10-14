# 8-16
#  导入 ：
# 选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。
# 在主程序文件中，使用下述各种方法导入这个函数，再调用它：

# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import one_func_module
from one_func_module import print_result
from  one_func_module import print_result as pr
import one_func_module as ofm
from one_func_module import *

i = 1
one_func_module.print_result(i)
i = i + 1

print_result(i)
i = i + 1

pr(i)
i = i + 1

ofm.print_result(i)
