# 9-7
# 管理员 ：
# 管理员是一种特殊的用户。
# 编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。
# 添加一个名为privileges 的属性，
# 用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。
# 编写一个名为show_privileges() 的方法，它显示管理员的权限。
# 创建一个Admin 实例，并调用这个方法。
class User:
    def __init__(self, first_name, last_name, info):
        self.first_name = first_name
        self.last_name = last_name
        self.info = info

    def describe_user(self):
        print('{} {} is a {}'.format(self.first_name, self.last_name, self.info))


class Admin(User):
    def __init__(self, first_name, last_name, info, *privileges):
        super().__init__(first_name, last_name, info)
        self.privileges = list(privileges)

    def show_privileges(self):
        print(self.privileges)


admin = Admin('mike', 'liu', 'dancer', 'can add post', 'can delete post', 'can ban user')
admin.show_privileges()
