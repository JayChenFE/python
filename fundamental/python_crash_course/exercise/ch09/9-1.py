# 9-1
# 餐馆 ：
# 创建一个名为Restaurant 的类，
# 其方法__init__()
# 设置两个属性：restaurant_name 和cuisine_type 。
# 创建一个名为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，
# 其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

from restaurant import Restaurant


restaurant = Restaurant('ChinaTown', 'Chinese-Food')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
