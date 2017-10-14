
class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print('restaurant {} is a {} restaurant'.format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print('restaurant {} is now open'.format(self.restaurant_name))


