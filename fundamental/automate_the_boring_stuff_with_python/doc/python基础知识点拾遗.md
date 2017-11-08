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
```

