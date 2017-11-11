'''编写一个名为printTable()的函数，
它接受字符串的列表的列表，将它显示在组织良好的表格中，每列右对齐。
假定所有内层列表都包含同样数目的字符串。例如，
该值可能看起来像这样：

tableData = [
['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

你的printTable()函数将打印出：
 apples  Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose'''


def printTable(dataLists):
    colCount = len(dataLists)
    rowCount = len(dataLists[0])
    colWidths = [0] * colCount

    for index in range(colCount):
        colWidths[index] = len(max(dataLists[index], key=len))

    for rowIndex in range(rowCount):
        list = []
        for colIndex in range(colCount):
            list.append(dataLists[colIndex][rowIndex].rjust(colWidths[colIndex]))

        print(' '.join(list))


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
