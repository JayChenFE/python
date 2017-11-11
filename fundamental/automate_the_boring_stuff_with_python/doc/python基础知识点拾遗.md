[TOC]



## python基础知识点拾遗

## 控制流

### 1.三个布尔操作符

`AND` `OR`  `NOT` 

## 函数

### 2.`None` 值

​    	在`Python` 中有一个值称为`None`，它表示没有值。`None `是`NoneType` 数据类型
的唯一值（其他编程语言可能称这个值为`null`、`nil` 或`undefined`)

### 3.关键字参数

`print()` 函数自动在传入的字符串末尾添加了换行符。可以设置`end `关键字参数，将它变成另一个字符串。

```python
print('Hello', end='')
print('World')
```

输出:

```python
HelloWorld
```



传入sep 关键字参数，替换掉默认的分隔字符串

```python
>>> print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice
```

### 4.global 语句

在函数的顶部有`global eggs` 这样的代码，它就告诉`Python`，“在这个函数中，`eggs `指的是全局变量，所以不要用这个名字创建一个局部变量。

```python
def spam():
  	global eggs
  	eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# spam
```

在一个函数中，一个变量要么总是全局变量，要么总是局部变量。<br>函数中的代码没有办法先使用名为`eggs` 的局部变量，稍后又在同一个函数中使用全局`eggs `变量。<br>如果想在一个函数中修改全局变量中存储的值，就必须对该变量使用`global`语句。

下面的代码会报错:

```python
def spam():
print(eggs) # ERROR!
	eggs = 'spam local'
	eggs = 'global'
spam()
```

### 5.`/`表示浮点数除法,结果一定为浮点数;`//`表示整数除法,结果向下取整.

```python
>>> 5/5
1.0
>>> 5//2
2
>>> 19//4
4
>>> 5.2//2
2.0
```

## 列表

### 6.列表连接和列表复制

```python
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam

[1, 2, 3, 'A', 'B', 'C']
```

### 7.列表的多重赋值技巧

类似于`ES6`解构赋值:

```python
>>> cat = ['fat', 'black', 'loud']
>>> size, color, disposition = cat
```

变量的数目和列表的长度必须严格相等，否则`Python` 将给出`ValueError`

### 8.列表删除元素

- 如果知道想要删除的值在列表中的下标，`del 语句`就很好用。

  ```python
  >>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
  >>> del(spam[1])
  >>> spam
  ['cat', 'rat', 'cat', 'hat', 'cat']
  ```

  ​

- 如果知道想要从列表中删除的值，`remove()方法`就很好用。

  ```python
  >>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
  >>> spam.remove('cat')
  >>> spam
  ['bat', 'rat', 'cat', 'hat', 'cat']
  ```

  ​

### 9.Python 中缩进规则的例外

在源代码文件中，列表实际上可以跨越几行。这些行的缩进并不重要。<br>Python 知道，没有看到结束方括号，列表就没有结束

下面的代码使合法的:

```python
spam = ['apples',
'oranges',
				'bananas',
'cats']
print(spam)
```

也可以在行末使用续行字符\，将一条指令写成多行。<br>可以把\看成是“这条指令在下一行继续”。\续行字符之后的一行中，缩进并不重要。<br>例如，下面是有效的Python 代码：

```python
print('Four score and seven ' + \
'years ago...')
```

### 10.字符串是“不可变的”

尝试对字符串中的一个字符重新赋值，将导致`TypeError` 错误:

```
>>> name = 'Zophie a cat'
>>> name[7] = 'the'
Traceback (most recent call last):
File "<pyshell#50>", line 1, in <module>
name[7] = 'the'
TypeError: 'str' object does not support item assignment
```



字符串的正确方式，是使用切片和连接:

```python
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'

```

### 11. 元组像字符串一样，是不可变的。元组不能让它们的值被修改、添加或删除。

如果元组中只有一个值，你可以在括号内该值的后面跟上一个逗号，表明这种情况。<br>否则，Python 将认为，你只是在一个普通括号内输入了一个值。<br>逗号告诉Python，这是一个元组（不像其他编程语言，Python 接受列表或元组中最后表项后面跟的逗号）

```python
>>> type('hello')
 <class 'str'>
 >>> type(('hello'))
 <class 'str'>
 >>> type(('hello',))
 <class 'tuple'>
```
### 12.传递引用

```python
def eggs(someParameter):
	someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)
```

输出

```
[1, 2, 3, 'Hello']
```

尽管`spam`和`someParameter` 包含了不同的引用，但它们都指向相同的列表

### 13.浅拷贝&深拷贝

`copy `模块的`copy()`和`deepcopy()`函数

- copy.copy浅拷贝
- copy.deepcopy深拷贝

## 字典

### 14.检查字典中是否存在键或值

```python
>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()
True
>>> 'Zophie' in spam.values()
True
>>> 'color' in spam.keys()
False
>>> 'color' not in spam.keys()
True
>>> 'color' in spam
False
```

`'color' in spam` 本质上是一个简写版本。相当于`'color'in spam.keys()`

### 15.`get()`方法和`setdefault()`方法

字典有一个`get()`方法，它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值。

`dict_instance.get(key,default_val)`

字典的`setdefault()`方法设定默认值

`dict_instance.setdefault(key,default_val)`返回该键的值

### 16.`pprint()`和`pformat()`函数

- 如果程序中导入`pprint `模块，就可以使用`pprint()`和`pformat()`函数，它们将“漂亮打印”一个字典的字

- 如果希望得到漂亮打印的文本作为字符串，而不是显示在屏幕上，那就调用`pprint.pformat()`。

  下面两行代码是等价的：

  ```python
  pprint.pprint(someDictionaryValue)
  print(pprint.pformat(someDictionaryValue))
  ```

## 字符串

### 18.转义字符

| 转义字符 | 打印为  |
| :--: | :--: |
|  \'  | 单引号  |
|  \"  | 双引号  |
|  \t  | 制表符  |
|  \n  | 换行符  |
| \\\  | 倒斜杠  |

### 19.原始字符串

 可以在字符串开始的引号之前加r，使它成为原始字符串。<br>“原始字符串”完全忽略所有的转义字符

  如果输入的字符串包含许多倒斜杠，比如下一章中要正则表达式字符串，那么原始字符串就很有用。

### 20.用三重引号的多行字符串

“三重引号”之间的所有引号、制表符或换行，都被认为是字符串的一部分。<br>Python 的代码块缩进规则不适用于多行字符串。

下面的代码是等价的

```python
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')
```

```python
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
```

### 21.有用的字符串方法

#### 表格

|          方法           |            说明             |
| :-------------------: | :-----------------------: |
|       `upper()`       |                           |
|       `lower()`       |                           |
|      `isupper()`      |                           |
|      `islower()`      |                           |
| `isalpha()`返回`True `  |       字符串只包含字母，并且非空       |
|  `isalnum()`返回`True`  |   字符串不包含字母和数字以外的字符，并且非空   |
| `isdecimal()`返回`True` |      字符串只包含数字字符，并且非空      |
|  `isspace()`返回`True`  | 字符串不包含空格、制表符和换行以外的字符，并且非空 |
|  `istitle()`返回`True`  | 字符串仅包含以大写字母开头、后面都是小写字母的单词 |

#### `join()`和`split()`的默认参数是空格 

#### 用`rjust()`、`ljust()`和`center()`方法对齐文本 

`rjust()`和`ljust()` 字符串方法第一个参数是一个整数长度，用于对齐字符串

第二个可选参数将指定一个填充字符，取代空格字符

```python
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20)
'               Hello'
>>> 'Hello World'.rjust(20)
' 		  Hello World'
>>> 'Hello'.ljust(10)
'Hello 		'
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
```

`'Hello'.rjust(10)`是说我们希望右对齐，将`'Hello'` 放在一个长度为10 的字符串中

```python
>>>'Hello'.center(20)
>>>'       Hello     '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

#### 用`strip()`、`rstrip()`和`lstrip()`删除空白字符 

`strip()`字符串方法将返回一个新的字符串，它的开头或末尾都没有空白字符。 
`lstrip()`和`rstrip()`方法将相应删除左边或右边的空白字符。



有一个可选的字符串参数，指定两边的哪些字符应该删除 

```python
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'
```

`strip('ampS')` 做的事情和`strip('mapS')`或`strip('Spam')`一样。 

#### 用`pyperclip` 模块拷贝粘贴字符串 

`pyperclip ` 这个`第三方模块` 有`copy()`和`paste()` 函数

```python
import  pyperclip
pyperclip.copy(str)  #内存=>剪切板
text = pyperclip.paste(str) #剪切板=>内存
```



#### 批处理

pw.py需要一个参数account

```bat
@py.exe C:\Python34\pw.py %*
@pause
```

上面的命令保存为 pw.bat

Win-R，再输入pw <account name>。