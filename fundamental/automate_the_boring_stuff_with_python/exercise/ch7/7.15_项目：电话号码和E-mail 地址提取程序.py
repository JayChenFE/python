'''
项目：电话号码和E-mail 地址提取程序
假设你有一个无聊的任务，要在一篇长的网页或文章中，找出所有电话号码和邮件地址。
如果手动翻页，可能需要查找很长时间。
如果有一个程序，可以在剪贴板的文本中查找电话号码和E-mail 地址，
那你就只要按一下Ctrl-A 选择所有文本，按下Ctrl-C 将它复制到剪贴板，然后运行你的程序。
它会用找到的电话号码和E-mail地址，替换掉剪贴板中的文本。

你的电话号码和E-mail 地址提取程序需要完成以下任务：

从剪贴板取得文本。
找出文本中所有的电话号码和E-mail 地址。
将它们粘贴到剪贴板。
现在你可以开始思考，如何用代码来完成工作。代码需要做下面的事情：
  使用pyperclip 模块复制和粘贴字符串。
  创建两个正则表达式，一个匹配电话号码，另一个匹配E-mail 地址。
  对两个正则表达式，找到所有的匹配，而不只是第一次匹配。
  将匹配的字符串整理好格式，放在一个字符串中，用于粘贴。
  如果文本中没有找到匹配，显示某种消息。
这个列表就像项目的路线图。在编写代码时，可以独立地关注其中的每一步。
'''
# ! python3

import re

import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?    #area code
    (\s|-|\.)?            #seperator
    (\d{3})               #first three digits
    (\s|-|\.)             #seperator
    (\d{4})               #last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    #username
    @                    #symbol
    [a-zA-Z0-9.-]+       #domain name
    (\.[a-zA-Z]{2.4})    #dot something
    )''', re.VERBOSE)

# Find matches in the clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])

    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to the clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email matches were found.')
