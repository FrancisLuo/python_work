from car import Car
class Battery(object):
    """电池电量更新 及里程显示"""
    def __init__(self):
        self.b_size = 70
    def update_battery(self):
        if self.b_size != 85:
            self.b_size = 85
    def get_range(self):
        miles_range = self.b_size * 3.5
        message = "This car can go approximately " + str(miles_range)
        print message

class ElectricalCar(Car):
    """电动汽车"""
    def __init__(self, make, model, year):
        super(ElectricalCar, self).__init__(make, model, year)
        self.battery = Battery()
