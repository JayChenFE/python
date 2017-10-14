# 6-11
# 城市 ：
# 创建一个名为cities 的字典，
# 其中将三个城市名用作键；对于每座城市，都创建一个字典，
# 并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含country 、population 和fact 等键。
# 将每座城市的名字以及有关它们的信息都打印出来。

cities = {
    'shanghai': {
        'country': 'China',
        'population': '200,000,000'
    },
    'tokyo': {
        'country': 'Japan',
        'population': '150,000,000'
    }
}

for city,info in cities.items():
    print("\n{}'s info is: ".format(city))
    for k,v in info.items():
        print('\t{} : {}'.format(k,v))
