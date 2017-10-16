# 10-12
# 记住喜欢的数字 ：
# 将练习10-11中的两个程序合而为一。
# 如果存储了用户喜欢的数字，就向用户显示它，
# 否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期的那样工作。

import os,json

file_name = 'favourite.json'
with open(file_name,'a+') as f:
    if f.read():
        num = json.load(file_name)
        print("I know your favorite number! It's " + num)
    else:
        num = input('plz input your favourite number : ')
        json.dump(num,f)
        print('your favourite number has been saved')
