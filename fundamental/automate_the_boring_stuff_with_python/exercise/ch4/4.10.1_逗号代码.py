# 假定有下面这样的列表：
# spam = ['apples', 'bananas', 'tofu', 'cats']
# 编写一个函数，它以一个列表值作为参数，返回一个字符串。
# 该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入and。
# 例如，将前面的spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。
# 但你的函数应该能够处理传递给它的任何列表

def list_to_str(listvalue):
    res = listvalue[:-1]
    res.append('and ' + listvalue[-1])
    return (', '.join(res))


spam = ['apples', 'bananas', 'tofu', 'cats']

print(list_to_str(spam))
