# 9-8
# 权限 ：
# 编写一个名为Privileges 的类，
# 它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。
# 将方法show_privileges() 移到这个类中。
# 在Admin 类中，将一个Privileges 实例用作其属性。
# 创建一个Admin 实例，并使用方法show_privileges() 来显示其权限。

class User:
    def __init__(self, first_name, last_name, info):
        self.first_name = first_name
        self.last_name = last_name
        self.info = info

    def describe_user(self):
        print('{} {} is a {}'.format(self.first_name, self.last_name, self.info))


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, info, *privileges):
        super().__init__(first_name, last_name, info)
        self.privileges = Privileges(list(privileges))


admin = Admin('mike', 'liu', 'dancer', 'can add post', 'can delete post', 'can ban user')
admin.privileges.show_privileges()
