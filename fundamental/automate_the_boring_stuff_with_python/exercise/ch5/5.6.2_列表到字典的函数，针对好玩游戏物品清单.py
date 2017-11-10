# 假设征服一条龙的战利品表示为这样的字符串列表：
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# 写一个名为addToInventory(inventory, addedItems)的函数，
# 其中inventory 参数是一个字典，表示玩家的物品清单（像前面项目一样），
# addedItems 参数是一个列表， 就像dragonLoot。

# addToInventory()函数应该返回一个字典，表示更新过的物品清单。
# 请注意，列表可以包含多个同样的项

# 你的代码看起来可能像这样：

# def addToInventory(inventory, addedItems):
#   # your code goes here
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)

# 前面的程序（加上前一个项目中的displayInventory()函数）将输出如下：

# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# Total number of items: 48

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v

    print("Total number of items: " + str(item_total))


def addToInventory(inventory,addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1


inv = {'gold coin': 42,'rope': 1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
addToInventory(inv,dragonLoot)
displayInventory(inv)
