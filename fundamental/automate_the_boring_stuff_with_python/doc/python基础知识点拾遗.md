## python基础知识点拾遗

1.三个布尔操作符

`AND` `OR`  `NOT` 

2.`None` 值

​    	在`Python` 中有一个值称为`None`，它表示没有值。`None `是`NoneType` 数据类型
的唯一值（其他编程语言可能称这个值为`null`、`nil` 或`undefined`)

3.`print()` 函数自动在传入的字符串末尾添加了换行符。可以设置`end `关键字参数，将它变成另一个字符串。

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

4.global 语句

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

5. `/`表示浮点数除法	,结果一定为浮点数;`//`表示整数除法,结果向下取整.

   ​

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

6.列表连接和列表复制

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

7.列表的多重赋值技巧

类似于`ES6`解构赋值:

```python
>>> cat = ['fat', 'black', 'loud']
>>> size, color, disposition = cat
```

变量的数目和列表的长度必须严格相等，否则`Python` 将给出`ValueError`

8.列表删除元素

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

9.Python 中缩进规则的例外

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

10.字符串是“不可变的”

尝试对字符串中的一个字符重新赋值，将导致`TypeError` 错误:

```python
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

11. 元组像字符串一样，是不可变的。元组不能让它们的值被修改、添加或删除。

   ```python
    >>> type('hello')
    <class 'str'>
    >>> type(('hello'))
    <class 'str'>
    >>> type(('hello',))
    <class 'tuple'>
   ```

     ​