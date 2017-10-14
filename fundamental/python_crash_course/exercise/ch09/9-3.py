# 9-3
# 用户 ：
# 创建一个名为User 的类，
# 其中包含属性first_name 和last_name ，
# 还有用户简介通常会存储的其他几个属性。
# 在类User 中定义一个名为describe_user() 的方法，它打印用户信息摘要；
# 再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User:
    def __init__(self, first_name, last_name, info):
        self.first_name = first_name
        self.last_name = last_name
        self.info = info

    def describe_user(self):
        print('{} {} is a {}'.format(self.first_name, self.last_name, self.info))


jay = User('jakie', 'chen', 'programmer')
mike = User('mike', 'jackson', 'singer')
jay.describe_user()
mike.describe_user()
