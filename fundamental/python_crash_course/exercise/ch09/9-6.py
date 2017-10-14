# 9-6 冰淇淋小店 ：
# 冰淇淋小店是一种特殊的餐馆。
# 编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant 类。
# 这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。
# 创建一个IceCreamStand 实例，并调用这个方法。

from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, name, type, *ice_creams):
        super().__init__(name, type)
        self.flavors = ice_creams

    def show_ice(self):
        print(self.flavors)


ice = IceCreamStand('2', '1', 'milk','chocolate')
ice.show_ice()
