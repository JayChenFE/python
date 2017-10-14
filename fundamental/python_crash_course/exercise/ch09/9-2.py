# 9-2
# 三家餐馆 ：
# 根据你为完成练习9-1而编写的类创建三个实例，
# 并对每个实例调用方法describe_restaurant() 。

from restaurant import Restaurant

r1 = Restaurant('China-Town', 'Chinese-Food')
r2 = Restaurant('KFC', 'Fast-Food')
r3 = Restaurant('Prezzo', 'Italian Cuisine')

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()
