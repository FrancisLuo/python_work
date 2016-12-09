
class Restaurant(object):
    def __init__(self, restaurant_name, restaurant_location):
        self.restaurant_name = restaurant_name
        self.restaurant_location = restaurant_location
        self.number_served = 0
    def describe_restaurant(self):
        description = self.restaurant_name + ", which is located in " + self.restaurant_location
        print description
    def set_number_served(self, number_served):
        if number_served < 0:
            print "please input the right number"
        else:
            self.number_served = number_served
            print "you have set the number of people we need to serve to " + str(self.number_served)
    def increment_number_served(self, increment_number):
        self.number_served += increment_number
        print "the number we served have been increased to " + str(self.number_served)

def make_shirt(shirt_size, shirt_motto="change the world"):
    print "the T-shirt's size is " + str(shirt_size) + ", and the motto is " + shirt_motto.title()

def make_pizza(*toppings):
    print toppings

def build_profile(first_name, last_name, **user_info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_restaurant = Restaurant('newbee', 'san francisco')
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(40)
my_restaurant.increment_number_served(60)
my_restaurant.set_number_served(-49)
